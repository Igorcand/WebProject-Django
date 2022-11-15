from django.shortcuts import render, redirect
from django.contrib.auth import logout

def home(request):
    return render(request, 'home/home.html')

def my_logout(request):
    logout(request)
    return render(request, 'home/home.html')

# CLASSES BASED VIEWS

#Utilizando a classe mais simples, a View, nos conseguimos renderizar htmls e definir funções dentro da classe para cada método http
from django.http import HttpResponse
from django.views import View
class MyView(View):
    def get(self, request, *args, **kwargs):
        #return HttpResponse('hello world')
        response = render(request, 'home/home3.html')
        response.set_cookie('cor', 'blue')
        return response
    
    def post(self, request, *args, **kwargs):
        return HttpResponse('hello world feito em post')


# No caso abaixo, é outro exemplo de CBV (Classes based views). Onde nos utilizamos o sistema de heraças de classes no python, para herdar atributos da classe chamada TemplateView, e configuramos nossa propria classe para home page chamada HomePageView
from django.views.generic.base import TemplateView
class HomePageView(TemplateView):
    template_name = 'home3.html'


    def get_context_data(self, **kwargs):
        #O super() é utilizado entre heranças de classes, ele nos proporciona extender/subscrever métodos de uma super classe (classe pai) para uma sub classe (classe filha), atrávez dele definimos um novo comportamento para um determinado método construido na classe pai e herdado pela classe filha.
        context = super().get_context_data(**kwargs)
        context['testando'] = 'Adicionando valores por método de herança'
        return context



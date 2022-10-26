from django.shortcuts import render, redirect, get_object_or_404
from django.urls import is_valid_path
from .models import Person
from django.http import HttpResponse
from .form import PersonForm
from django.contrib.auth.decorators import login_required

@login_required
def people_list(request):
    persons = Person.objects.all()
    return render(
        request, 'person.html', {'persons': persons})

@login_required
def person_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form':form})

def home(request):
    return render(request, 'index.html')

@login_required
def person_update(request, id):
    person = get_object_or_404(Person, pk=id) 
    form = PersonForm(request.POST or None,  request.FILES or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form':form})

@login_required
def person_delete(request, id):
    person = get_object_or_404(Person, pk=id) 
    if request.method == 'POST':
        person.delete()
        return redirect('person_list')
    return render(request, 'person_delete_confirm.html', {'person':person})

# CLASSES BASED VIEWS

# ListView

# A função herdada na classe chamada ListView, serve para fazer uma listagem dos valores que estão cadastrados no banco de dados, como se fosse, por baixo dos panos, 'Person.objects.all()', e ele adiciona em uma variável padrão chamada object_list. Feito isso, podemos apenas acessas a variável no template, adicionar no html
from django.views.generic.list import ListView
class PersonListView(ListView):
    #Se não falarmos qual é o template name, o django irá procurar dentro da sua app, em templates, uma outra pasta com o mesmo nome da app, com o arquivo com o nome do model, todo em minusculo, + _list. Então o arquivo seria person_list.html, na raiz app_name/templates/app_name/modelname_list.html
    model = Person

# DetailView

# Da mesma forma que o ListView pega todos os valores da tabela no banco por debaixo dos panos, o DetailView seria como um filter_by_id, pegando todas as informações pela primary key
from django.views.generic.detail import DetailView
class PersonDetailView(DetailView):
    model = Person

# CreateView
#É uma view para criação de formularios
from django.views.generic.edit import CreateView
class PersonCreateView(CreateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = '/clientes/person_list/'

# UpdateView

#É uma view para edição de formularios
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
class PersonUpdateView(UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = reverse_lazy('person_list_cbv')

# DeleteView

#É uma view para deletar valores
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
class PersonDeleteView(DeleteView):
    model = Person
    #success_url = reverse_lazy('person_list_cbv')

    #Utilizando a função abaixo, nos podemos manipular o objeto de entrada, e depois redirecionamos, ao invés de só redirecionar
    def get_success_url(self):
        return reverse_lazy('person_list_cbv')
from django.urls import path
from .views import home, my_logout, HomePageView, MyView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', home, name='home'),
    path('logout/', my_logout, name='my_logout'),

    # CLASSES BASED VIEWS
    path('view', MyView.as_view()),
    # No caso abaixo, é um exemplo de CBV (Classes based views). Onde não é preciso criar uma view para apenas mostrar um html, o que conseguimos fazer com apenas uma classe chamada TemplateView. Ou seja, a TemplateView apenas mostra o html sem poder acrescentar informações no html
    path('home2', TemplateView.as_view(template_name='home2.html')),
    #Já esse exemplo, nos conseguimos acrescentar informações com uma fácil alterações de heranças de classes, customizando uma classe chamada HomePageView
    path('home3', HomePageView.as_view(template_name='home3.html')),


]
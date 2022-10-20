from django.shortcuts import render, redirect, get_object_or_404
from django.urls import is_valid_path
from .models import Person
from django.http import HttpResponse
from .form import PersonForm

# Create your views here.

def people_list(request):
    persons = Person.objects.all()
    return render(
        request, 'person.html', {'persons': persons})

def person_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form':form})

def home(request):
    return render(request, 'index.html')

def person_update(request, id):
    person = get_object_or_404(Person, pk=id) 
    form = PersonForm(request.POST or None,  request.FILES or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form':form})


def person_delete(request, id):
    person = get_object_or_404(Person, pk=id) 
    if request.method == 'POST':
        person.delete()
        return redirect('person_list')
    return render(request, 'person_delete_confirm.html', {'person':person})
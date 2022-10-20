from django.urls import path
from .views import people_list, person_new, home, person_update

urlpatterns = [
    path('list/', people_list, name="person_list"),
    path('new/', person_new, name="person_new"),
    path('update/<int:id>/', person_update, name="person_update"),
    path('delete/<int:id>/', person_update, name="person_delete"),
    path('home/', home),
]
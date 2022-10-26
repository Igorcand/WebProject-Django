from django.urls import path
from .views import people_list, person_new, home, person_update, person_delete, PersonListView, PersonDetailView, PersonCreateView, PersonUpdateView, PersonDeleteView

urlpatterns = [
    path('list/', people_list, name="person_list"),
    path('new/', person_new, name="person_new"),
    path('update/<int:id>/', person_update, name="person_update"),
    path('delete/<int:id>/', person_delete, name="person_delete"),
    path('home/', home),
    # CLASSES BASED VIEWS
    path('person_list/', PersonListView.as_view(),name='person_list_cbv'),
    path('person_detail/<int:pk>/', PersonDetailView.as_view(), name='person_detail_cbv'),
    path('person_update/<int:pk>/', PersonUpdateView.as_view(), name='person_update_cbv'),
    path('person_delete/<int:pk>/', PersonDeleteView.as_view(), name='person_delete_cbv'),

    path('person_create/', PersonCreateView.as_view(), name='person_form_cbv'),
    


]
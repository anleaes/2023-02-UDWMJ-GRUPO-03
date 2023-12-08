from django.urls import path
from . import views

app_name = 'vaccinationregistries'

urlpatterns = [
    path('', views.list_vaccinationregistries, name='list_vaccinationregistries'),
    path('adicionar/', views.add_vaccinationregistry, name='add_vaccinationregistry'),
    path('editar/<int:id_vaccinationregistry>/', views.edit_vaccinationregistry, name='edit_vaccinationregistry'),
    path('excluir/<int:id_vaccinationregistry>/', views.delete_vaccinationregistry, name='delete_vaccinationregistry'),
]
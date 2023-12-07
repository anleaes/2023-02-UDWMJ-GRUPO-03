from django.urls import path
from . import views

app_name = 'patient'

urlpatterns = [
    path('', views.list_patients, name='list_patients'),
    path('adicionar/', views.add_patient, name='add_patient'),
    path('editar/<int:id_patient>/', views.edit_patient, name='edit_patient'),
    path('excluir/<int:id_patient>/', views.delete_patient, name='delete_patient'),
]
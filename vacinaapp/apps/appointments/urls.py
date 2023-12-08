from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('', views.list_appointments, name='list_appointments'),
    path('adicionar/<int:id_patient>/', views.add_appointment, name='add_appointment'),
    path('excluir/<int:id_appointment>/', views.delete_appointment, name='delete_appointment'),
    path('excluir-vacina/<int:id_appointment_vaccine>/', views.delete_appointment_vaccine, name='delete_appointment_vaccine'),
    path('adicionar-vacina/<int:id_appointment>/', views.add_appointment_vaccine, name='add_appointment_vaccine'),
]
from django.urls import path
from . import views

app_name = 'healthcenters'

urlpatterns = [
    path('', views.list_healthcenters, name='list_healthcenters'),
    path('adicionar/', views.add_healthcenter, name='add_healthcenter'),
    path('editar/<int:id_healthcenter>/', views.edit_healthcenter, name='edit_healthcenter'),
    path('excluir/<int:id_healthcenter>/', views.delete_healthcenter, name='delete_healthcenter'),
]

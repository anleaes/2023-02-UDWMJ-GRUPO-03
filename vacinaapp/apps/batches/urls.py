from django.urls import path
from . import views

app_name = 'batches'

urlpatterns = [
    path('', views.list_batches, name='list_batches'),
    path('adicionar/', views.add_batch, name='add_batch'),
    path('editar/<int:id_batch>/', views.edit_batch, name='edit_batch'),
    path('excluir/<int:id_batch>/', views.delete_batch, name='delete_batch'),
]
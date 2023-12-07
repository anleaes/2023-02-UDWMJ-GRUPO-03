from django.urls import path
from . import views

app_name = 'professionals'

urlpatterns = [
    path('', views.list_professionals, name='list_professionals'),
    path('adicionar/', views.add_professional, name='add_professional'),
    path('editar/<int:id_professional>/', views.edit_professional, name='edit_professional'),
    path('excluir/<int:id_professional>/', views.delete_professional, name='delete_professional'),
]

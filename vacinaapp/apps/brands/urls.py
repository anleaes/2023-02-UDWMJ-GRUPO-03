from django.urls import path
from . import views

app_name = 'brands'

urlpatterns = [
    path('', views.list_brands, name='list_brands'),
    path('adicionar/', views.add_brand, name='add_brand'),
    path('editar/<int:id_brand>/', views.edit_brand, name='edit_brand'),
    path('excluir/<int:id_brand>/', views.delete_brand, name='delete_brand'),
]
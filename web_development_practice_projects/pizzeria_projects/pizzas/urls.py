""" Define URL for pizzas app"""

from django.urls import path
from . import views

app_name = 'pizzas'

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('menu/<int:pizza_id>/', views.pizza, name='pizza'),
    path('add_pizza/', views.add_pizza, name='add_pizza'),
    path('add_topping/<int:pizza_id>/', views.add_topping, name='add_topping'),
    path('edit_topping/<int:topping_id>/', views.edit_topping, name='edit_topping'),
    path('delete_pizza/<int:pizza_id>/', views.delete_pizza, name='delete_pizza'),
    path('delete_topping/<int:topping_id>/', views.delete_topping, name='delete_topping'),
]

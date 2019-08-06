from django.urls import path
from . import views

#app_name = 'menu'
urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('menu_edit/<int:pk>/', views.edit_menu, name='menu_edit'),
    path('menu_detail/<int:pk>/', views.menu_detail, name='menu_detail'),
    path('menu_item/<int:pk>/', views.item_detail, name='item_detail'),
    path('menu_create_new/', views.create_new_menu, name='menu_new'),
]
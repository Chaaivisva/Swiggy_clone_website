from django.urls import path
from . import views
from .views import Food_item_list
urlpatterns = [
  path('about/', views.about, name='about'),
  path('home/', views.home, name='home'),
  path('restaurants/', views.restaurant_list, name='restaurant_list'),
  path('restaurants/<int:restaurant_id>/', Food_item_list.as_view(), name='food_item_list'),
  path('social/signup/', views.signup_redirect, name='signup_redirect'),
  # path('order/', views.order, name= 'order'),
  # path('add_menu_item/', views.add_menu_item, name='add_menu_item'),
]
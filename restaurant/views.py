from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django. contrib import messages
from django.views import View

def about(request):
  return render(request, 'customer/about.html')

def home(request):
  return render(request, 'customer/home.html')

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'customer/restaurant_list.html', {'restaurants': restaurants})

class Food_item_list(View):
    def get(self, request, restaurant_id, *args, **Kwargs):
         restaurant = Restaurant.objects.get(id=restaurant_id)
         food_items = MenuItem.objects.filter(restaurant=restaurant)
         return render(request, 'customer/food_item_list.html', {'restaurant': restaurant, 'food_items': food_items})
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')

        order_items = {
            'items' : []
        }

        items = request.POST.getlist('items[]')

        for item in items:
            menu_item = MenuItem.objects.get(pk = int(item))
            item_data = {
                'id' : menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price,
            }
            order_items['items'].append(item_data)
        
        price = 0
        item_ids = []

        for item in order_items['items']:
            price = price + item['price']
            item_ids.append(item['id'])
        order = OrderModel.objects.create(
             price=price,
             name = name,
             email = email,
             street = street,
             city = city,
             state = state,
             zip_code = zip_code,
        )
        
        order.items.add(*item_ids)

        context = {
            'items': order_items['items'],
            'price': price
        }
        return render(request, 'customer/order_confirmation.html', context)
def index(request):
   return render(request, 'index.html')

def signup(request):
   if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
          form.save()
          return redirect('index')
   else:
      form = UserCreationForm()
   return render(request, 'registration/signup.html',{
      'form': form
   })

def signup_redirect(request):
   messages.error(request, 'Something wrong here, it may be that you already have account !!')
   return redirect('index')

# @login_required
# def secret_page(request):
#    return render(request, 'secret_page.html')

# def SecretPage(LoginRequiredMixin ,TemplateView):
#    template_name = 'secret_page.html'

# 

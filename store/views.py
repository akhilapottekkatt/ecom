from django.shortcuts import render
from . models import *
from .models import OrderIteam

# Create your views here.

from django.shortcuts import render

def store(request):
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'store/store.html', context)


def cart(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created =Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		items = []
	context = {'items':items}
	return render(request, 'store/cart.html', context)



def checkout(request):
	context = {}
	return render(request, 'store/checkout.html', context)

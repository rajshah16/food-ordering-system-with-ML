from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .models import Customer
from .models import Order
from .models import OrderItem
from .models import Productbf
from .models import Productbev
from .models import Productchp
from .models import Productsoup
from .models import Productdessert
from .models import OrderItembf
from .models import OrderItembev
from .models import OrderItemchp
from .models import OrderItemsoup
from .models import OrderItemdessert
from django.http import JsonResponse
import json
# Create your views here.
def menu(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer , complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0 , 'shipping':False}
        cartItems = order['get_cart_items']
    menu = Product.objects.all()
    subcateory = Product.objects.values('subcategory')
    params = {'menu':menu }
    return render(request , 'menu/menu.html' , params)

def beverage(request):
    menu = Productbev.objects.all()
    params = {'menu':menu}
    return render(request , 'menu/beverages.html' , params)

def breakfast(request):
    menu = Productbf.objects.all()
    params = {'menu':menu}
    return render(request , 'menu/breakfast.html' , params)

def chapatis(request):
    menu = Productchp.objects.all()
    params = {'menu':menu}
    return render(request , 'menu/chapatis.html' , params)

def soup(request):
    menu = Productsoup.objects.all()
    params = {'menu':menu}
    return render(request , 'menu/soup.html' , params)

def dessert(request):
    menu = Productdessert.objects.all()
    params = {'menu':menu}
    return render(request , 'menu/dessert.html' , params)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer = customer , complete=False)
        items = order.orderitem_set.all()
        itemsbf = order.orderitembf_set.all()
        itemsbev = order.orderitembev_set.all()
        itemschp = order.orderitemchp_set.all()
        itemssoup = order.orderitemsoup_set.all()
        itemsdessert = order.orderitemdessert_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        itemsbf = []
        itemsbev = []
        itemschp = []
        itemssoup = []
        itemsdessert = []
        cartItems = order['get_cart_items']
        
    context = {'items':items , 'itemsbf':itemsbf , 'itemsbev':itemsbev , 'itemschp':itemschp , 'itemssoup':itemssoup , 'itemsdessert':itemsdessert}

    return render(request , 'menu/cart.html' , context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer = customer , complete=False)
        items = order.orderitem_set.all()
        itemsbf = order.orderitembf_set.all()
        itemsbev = order.orderitembev_set.all()
        itemschp = order.orderitemchp_set.all()
        itemssoup = order.orderitemsoup_set.all()
        itemsdessert = order.orderitemdessert_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        itemsbf = []
        itemsbev = []
        itemschp = []
        itemssoup = []
        itemsdessert = []
        cartItems = order['get_cart_items']
    context = {'items':items ,'itemsbf':itemsbf,'itemsbev':itemsbev ,'itemschp':itemschp, 'itemssoup':itemssoup, 'itemsdessert':itemsdessert,'order':order ,'cartItems':cartItems}
    
    return render(request , 'menu/checkout.html' , context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('ProductId:' , productId)
    customer = request.user.customer
    product = Product.objects.get(id = productId)
    order , created = Order.objects.get_or_create(customer=customer , complete=False)
    orderItem , created = OrderItem.objects.get_or_create(order=order , product = product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
		
    orderItem.save()
    if orderItem.quantity <=0:
        orderItem.delete()
	
    return JsonResponse('Item is added' , safe=False)

def updateItembf(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('ProductId:' , productId)
    customer = request.user.customer
    product = Productbf.objects.get(id = productId)
    order , created = Order.objects.get_or_create(customer=customer , complete=False)
    orderItem , created = OrderItembf.objects.get_or_create(order=order , product = product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
		
    orderItem.save()
    if orderItem.quantity <=0:
        orderItem.delete()
    return JsonResponse("Breakfast Item are updated" , safe=False)

def updateItembev(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('ProductId:' , productId)
    customer = request.user.customer
    product = Productbev.objects.get(id = productId)
    order , created = Order.objects.get_or_create(customer=customer , complete=False)
    orderItem , created = OrderItembev.objects.get_or_create(order=order , product = product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
		
    orderItem.save()
    if orderItem.quantity <=0:
        orderItem.delete()
    return JsonResponse("Beverages are updated" , safe=False)

def updateItemchp(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('ProductId:' , productId)
    customer = request.user.customer
    product = Productchp.objects.get(id = productId)
    order , created = Order.objects.get_or_create(customer=customer , complete=False)
    orderItem , created = OrderItemchp.objects.get_or_create(order=order , product = product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
		
    orderItem.save()
    if orderItem.quantity <=0:
        orderItem.delete()
    return JsonResponse("Chapatis are updated" , safe=False)

def updateItemsoup(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('ProductId:' , productId)
    customer = request.user.customer
    product = Productsoup.objects.get(id = productId)
    order , created = Order.objects.get_or_create(customer=customer , complete=False)
    orderItem , created = OrderItemsoup.objects.get_or_create(order=order , product = product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
		
    orderItem.save()
    if orderItem.quantity <=0:
        orderItem.delete()
    return JsonResponse("Soup is added" , safe=False)

def updateItemdessert(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('ProductId:' , productId)
    customer = request.user.customer
    product = Productdessert.objects.get(id = productId)
    order , created = Order.objects.get_or_create(customer=customer , complete=False)
    orderItem , created = OrderItemdessert.objects.get_or_create(order=order , product = product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
		
    orderItem.save()
    if orderItem.quantity <=0:
        orderItem.delete()
    return JsonResponse("Dessert is updated" , safe=False)
   
  
   
    
from django.shortcuts import render
from .models import Product
# Create your views here.
from .models import Order,OrderItem,ShippingInfo,Customer
from django.http import JsonResponse
import json
import datetime
from . utils import *
from django.contrib.auth import get_user_model

User = get_user_model()

def shop(request):
    data=cart_data(request)   
    cart_total=data['cart_total']
       

    context={
       "products":Product.objects.all(),
       "cart_total":cart_total

    }
    return render(request,"shop/shop.html",context )



def cart(request):
    data=cart_data(request)
    orderitems=data['orderitems']
    order=data['order']
    cart_total=data['cart_total']
       




    context={
       "orderitems":orderitems,
       "order":order,
       "cart_total":cart_total

     }

    return render(request,"shop/cart.html",context)



def checkout(request):

    
    data=cart_data(request)
    orderitems=data['orderitems']
    order=data['order']
    cart_total=data['cart_total']
        

    context={
       "orderitems":orderitems,
       "order":order,
       "cart_total":cart_total

     }
    

    return render(request,"shop/checkout.html",context)


def update_item(request):
    data=json.loads(request.body)
    product_id=data['product_id']
    action=data['action']
    customer=request.user.customer
    product=Product.objects.filter(id=product_id).first()
    order,created=Order.objects.get_or_create(customer=customer,complete=False)
    order_item,created=OrderItem.objects.get_or_create(order=order,product=product)
    if action == 'add':
        order_item.quantity= order_item.quantity + 1

    elif action == 'remove':
        order_item.quantity =order_item.quantity -1

    order_item.save()

    if order_item.quantity < 1:
       order_item.delete()

    return JsonResponse("hello mars",safe=False)


def process_order(request):
  
    data=json.loads(request.body)
    print("data",data)
    if request.user.is_authenticated:
        customer=request.user.customer
       
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
       

    else:
        order,customer=guest_order(data,request)
           
    total_price=float(data['userInfo']['total_price'])
    order.transaction_id=datetime.datetime.now().timestamp()
    if total_price==float(order.get_cart_total_price):
        order.complete=True
    order.save()

    if order.shipping ==True:
        ShippingInfo.objects.create(
            customer=customer,
            order=order,
            address=data['shippingInfo']['address'],
            city=data['shippingInfo']['city'],
            state=data['shippingInfo']['state'],
            zip_code=data['shippingInfo']['zip']



        )

    return JsonResponse ("goodboy",safe=False)



 
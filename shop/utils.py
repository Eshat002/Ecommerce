from . models import * 
import json

def cookie_cart(request):
    orderitems=[]
    order={'get_cart_total_price':0,"get_cart_total":0,"shipping":False}
    cart_total=order['get_cart_total']

    try:
        cart=json.loads(request.COOKIES['cart'])

    except:
            cart={}
    for i in cart:
        try:
            cart_total += cart[i]['quantity']

            product=Product.objects.filter(id=i).first()
            total_price_per_product=(product.price * cart[i]['quantity'])
            order['get_cart_total_price'] += total_price_per_product
            order['get_cart_total'] += cart[i]['quantity']
            orderitem={
                'product':{
                        "id":product.id,
                        "name":product.name,
                            "price":product.price,
                            "image":{"url":product.image.url}
                        },
                'quantity':cart[i]['quantity'],
                
                'total_price':total_price_per_product

            }
            orderitems.append(orderitem)

            if product.is_digital == False:
                order['shipping'] =True
        except:
            pass
    return {  "orderitems":orderitems,
       "order":order,
       "cart_total":cart_total}


def cart_data(request):
    if request.user.is_authenticated:
        customer=request.user.customer   
     
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        
        orderitems=order.orderitem_set.all()
        cart_total=order.get_cart_total
    else:
        # orderitems=[],
        # order={'get_cart_total_price':0,"get_cart_total":0,"shipping":False}
        # cart_total=order['get_cart_total']
        cookie_data=cookie_cart(request)
        orderitems=cookie_data['orderitems']
        order=cookie_data['order']
        cart_total=cookie_data['cart_total']

    return {  "orderitems":orderitems,
       "order":order,
       "cart_total":cart_total}



def guest_order(data,request):
    name = data['userInfo']['name']
    email = data['userInfo']['email']

    cookieData = cookie_cart(request)
    orderitems = cookieData['orderitems']
    

    customer, created = Customer.objects.get_or_create(
                email=email,
                
                )
        
    customer.name = name
    customer.save()
    
    

    order = Order.objects.create(
        customer=customer,
        complete=False,
        )

    for orderitem in orderitems:
        product = Product.objects.get(id=orderitem['product']['id'])
        created_orderitem = OrderItem.objects.create(
            product=product,
            order=order,
            quantity=orderitem['quantity'], # negative quantity = freebies
        )
    return order,customer

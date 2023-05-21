from django.urls import path
from . import views
urlpatterns = [
    path('', views.shop,name='shop'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('update-items/',views.update_item,name='update-items'),
    path('process-order/',views.process_order,name='process-order')
]

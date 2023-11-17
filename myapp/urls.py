from django.contrib import admin
from django.urls import path,include
from myapp.views import order,index,detail,cart_view,return_view,cancle_view
app_name='myapp'

urlpatterns = [
path('',index,name='index'), 
path('<int:product_id>/<slug:slug>',detail,name='detail'), 
path('cart/',cart_view,name='cart_view'),
path('order/',order,name='order'),
path('success/',return_view,name='return_view'),
path('cancle/',cancle_view,name='cancel_view'),
]

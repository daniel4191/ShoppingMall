from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<pk>[0-9]+/', views.profile, name='profile'),
    path('profile/<pk>[0-9]+/order_list/',
         views.order_list, name='order_list'),
    path('notice/', views.notice, name='notice'),
    path('notice/<pk>[0-9]+/',
         views.notice_detail, name='notice_detail'),
    path('<category_id>[0-9]+/',
         views.show_category, name='show_category'),
    path('detail/<pk>[0-9]+/',
         views.product_detail, name='product_detail'),
    path('<pk>[0-9]+/cart_or_buy/',
         views.cart_or_buy, name='cart_or_buy'),
    path('cart/<pk>[0-9]+/', views.cart, name='cart'),
    path('cart/<pk>[0-9]+/delete/',
         views.delete_cart, name='delete_cart'),

]

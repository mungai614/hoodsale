from django.contrib import admin
from django.urls import path
from hoodsaleapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_dashboard/', views.admin_dashboard, name='admin'),
    path('cart/', views.cart, name='cart'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('order/', views.order, name='order'),
    path('product/', views.product, name='product'),
    path('', views.shop, name='shop'),

]


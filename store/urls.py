from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('category/<slug:slug>/', views.category_detail, name='category'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('checkout/<int:product_id>/', views.checkout, name='checkout'),
    path('order-success/', views.order_success, name='order_success'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('it-support/', views.it_support, name='it_support'),
    path('it-support-request/', views.it_support_request, name='it_support_request'),
    path('it-support-success/', views.it_support_success, name='it_support_success'),
]

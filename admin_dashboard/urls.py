from django.urls import path
from . import views

app_name = 'admin_dashboard'

urlpatterns = [
    path('login/', views.admin_login, name='login'),
    path('logout/', views.admin_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('products/', views.products_list, name='products'),
    path('orders/', views.orders_list, name='orders'),
    path('messages/', views.contact_messages, name='messages'),
    path('mark-message-read/<int:message_id>/', views.mark_message_read, name='mark_message_read'),
    path('mark-order-completed/<int:order_id>/', views.mark_order_completed, name='mark_order_completed'),
    path('it-support/', views.it_support_requests, name='it_support_requests'),
    path('mark-it-request-in-progress/<int:request_id>/', views.mark_it_request_in_progress, name='mark_it_request_in_progress'),
    path('mark-it-request-completed/<int:request_id>/', views.mark_it_request_completed, name='mark_it_request_completed'),
]

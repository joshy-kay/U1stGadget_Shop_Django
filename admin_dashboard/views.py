from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from django.utils import timezone
from store.models import Product, Category, Order, ContactMessage, ITSupportRequest


def admin_login(request):
    """Custom admin login page"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard:dashboard')
        else:
            messages.error(request, 'Invalid credentials or insufficient permissions.')
    
    return render(request, 'admin_dashboard/login.html')


@login_required(login_url='admin_dashboard:login')
def admin_logout(request):
    """Custom admin logout"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('admin_dashboard:login')


@login_required(login_url='admin_dashboard:login')
def dashboard(request):
    """Main admin dashboard"""
    if not request.user.is_staff:
        return redirect('store:home')
    
    # Get statistics
    total_products = Product.objects.count()
    total_orders = Order.objects.count()
    total_contact_messages = ContactMessage.objects.count()
    unread_messages = ContactMessage.objects.filter(is_read=False).count()
    total_it_requests = ITSupportRequest.objects.count()
    pending_it_requests = ITSupportRequest.objects.filter(status='pending').count()
    
    # Get recent orders
    recent_orders = Order.objects.order_by('-created_at')[:5]
    
    # Get recent contact messages
    recent_messages = ContactMessage.objects.order_by('-created_at')[:5]
    
    # Get recent IT support requests
    recent_it_requests = ITSupportRequest.objects.order_by('-created_at')[:5]
    
    # Get products by category
    categories_with_count = Category.objects.annotate(product_count=Count('products'))
    
    # Get orders by status
    pending_orders = Order.objects.filter(is_completed=False).count()
    completed_orders = Order.objects.filter(is_completed=True).count()
    
    context = {
        'total_products': total_products,
        'total_orders': total_orders,
        'total_contact_messages': total_contact_messages,
        'unread_messages': unread_messages,
        'total_it_requests': total_it_requests,
        'pending_it_requests': pending_it_requests,
        'recent_orders': recent_orders,
        'recent_messages': recent_messages,
        'recent_it_requests': recent_it_requests,
        'categories_with_count': categories_with_count,
        'pending_orders': pending_orders,
        'completed_orders': completed_orders,
    }
    
    return render(request, 'admin_dashboard/dashboard.html', context)


@login_required(login_url='admin_dashboard:login')
def products_list(request):
    """Products management page"""
    if not request.user.is_staff:
        return redirect('store:home')
    
    products = Product.objects.all().order_by('-date_added')
    categories = Category.objects.all()
    
    # Filter by category
    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)
    
    context = {
        'products': products,
        'categories': categories,
        'selected_category': category_id,
    }
    
    return render(request, 'admin_dashboard/products.html', context)


@login_required(login_url='admin_dashboard:login')
def orders_list(request):
    """Orders management page"""
    if not request.user.is_staff:
        return redirect('store:home')
    
    orders = Order.objects.all().order_by('-created_at')
    
    # Filter by status
    status = request.GET.get('status')
    if status == 'pending':
        orders = orders.filter(is_completed=False)
    elif status == 'completed':
        orders = orders.filter(is_completed=True)
    
    context = {
        'orders': orders,
        'selected_status': status,
    }
    
    return render(request, 'admin_dashboard/orders.html', context)


@login_required(login_url='admin_dashboard:login')
def contact_messages(request):
    """Contact messages management page"""
    if not request.user.is_staff:
        return redirect('store:home')
    
    messages_list = ContactMessage.objects.all().order_by('-created_at')
    
    # Filter by read status
    filter_type = request.GET.get('filter')
    if filter_type == 'unread':
        messages_list = messages_list.filter(is_read=False)
    elif filter_type == 'read':
        messages_list = messages_list.filter(is_read=True)
    
    context = {
        'messages': messages_list,
        'selected_filter': filter_type,
    }
    
    return render(request, 'admin_dashboard/messages.html', context)


@login_required(login_url='admin_dashboard:login')
def mark_message_read(request, message_id):
    """Mark a contact message as read"""
    if not request.user.is_staff:
        return redirect('store:home')
    
    try:
        message = ContactMessage.objects.get(id=message_id)
        message.is_read = True
        message.save()
        messages.success(request, 'Message marked as read.')
    except ContactMessage.DoesNotExist:
        messages.error(request, 'Message not found.')
    
    return redirect('admin_dashboard:messages')


@login_required(login_url='admin_dashboard:login')
def mark_order_completed(request, order_id):
    """Mark an order as completed"""
    if not request.user.is_staff:
        return redirect('store:home')
    
    try:
        order = Order.objects.get(id=order_id)
        order.is_completed = True
        order.save()
        messages.success(request, 'Order marked as completed.')
    except Order.DoesNotExist:
        messages.error(request, 'Order not found.')
    
    return redirect('admin_dashboard:orders')


@login_required(login_url='admin_dashboard:login')
def it_support_requests(request):
    """IT Support requests management page"""
    if not request.user.is_staff:
        return redirect('store:home')
    
    requests_list = ITSupportRequest.objects.all().order_by('-created_at')
    
    # Filter by status
    status = request.GET.get('status')
    if status == 'pending':
        requests_list = requests_list.filter(status='pending')
    elif status == 'in_progress':
        requests_list = requests_list.filter(status='in_progress')
    elif status == 'completed':
        requests_list = requests_list.filter(status='completed')
    elif status == 'cancelled':
        requests_list = requests_list.filter(status='cancelled')
    
    context = {
        'requests': requests_list,
        'selected_status': status,
    }
    
    return render(request, 'admin_dashboard/it_support_requests.html', context)


@login_required(login_url='admin_dashboard:login')
def mark_it_request_in_progress(request, request_id):
    """Mark an IT support request as in progress"""
    if not request.user.is_staff:
        return redirect('store:home')
    
    try:
        request_obj = ITSupportRequest.objects.get(id=request_id)
        request_obj.status = 'in_progress'
        request_obj.save()
        messages.success(request, 'Request marked as in progress.')
    except ITSupportRequest.DoesNotExist:
        messages.error(request, 'Request not found.')
    
    return redirect('admin_dashboard:it_support_requests')


@login_required(login_url='admin_dashboard:login')
def mark_it_request_completed(request, request_id):
    """Mark an IT support request as completed"""
    if not request.user.is_staff:
        return redirect('store:home')
    
    try:
        request_obj = ITSupportRequest.objects.get(id=request_id)
        request_obj.status = 'completed'
        request_obj.completed_at = timezone.now()
        request_obj.save()
        messages.success(request, 'Request marked as completed.')
    except ITSupportRequest.DoesNotExist:
        messages.error(request, 'Request not found.')
    
    return redirect('admin_dashboard:it_support_requests')

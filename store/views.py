from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, ContactMessage, Order, ITSupportRequest
from .forms import ITSupportRequestForm


def test(request):
    """Simple test view to check if Django is working"""
    return render(request, 'store/test.html')


def home(request):
    """Home page view with featured products and hero banner"""
    try:
        featured_products = Product.objects.filter(is_featured=True, stock_status='in_stock')[:6]
        latest_products = Product.objects.filter(stock_status='in_stock').order_by('-date_added')[:8]
        categories = Category.objects.all()[:4]
    except Exception as e:
        # If database queries fail, return empty querysets
        featured_products = Product.objects.none()
        latest_products = Product.objects.none()
        categories = Category.objects.none()
    
    context = {
        'featured_products': featured_products,
        'latest_products': latest_products,
        'categories': categories,
    }
    return render(request, 'store/home.html', context)


def shop(request):
    """Shop page showing all products with filtering and pagination"""
    products = Product.objects.filter(stock_status='in_stock')
    categories = Category.objects.all()
    
    # Category filter
    category_slug = request.GET.get('category')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    # Pagination
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'selected_category': category_slug,
        'search_query': search_query or '',
    }
    return render(request, 'store/shop.html', context)


def category_detail(request, slug):
    """Category page showing products from a specific category"""
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, stock_status='in_stock')
    
    # Pagination
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'category': category,
        'page_obj': page_obj,
    }
    return render(request, 'store/category.html', context)


def product_detail(request, slug):
    """Product detail page"""
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(
        category=product.category, 
        stock_status='in_stock'
    ).exclude(id=product.id)[:4]
    
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'store/product_detail.html', context)


def checkout(request, product_id):
    """Checkout page with two options: store pickup or delivery"""
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        order_type = request.POST.get('order_type')
        
        if order_type == 'store_pickup':
            # Store pickup order
            order = Order.objects.create(
                full_name=request.POST.get('full_name'),
                phone_number=request.POST.get('phone_number'),
                product=product,
                order_type='store_pickup',
                notes=request.POST.get('notes', '')
            )
            messages.success(request, 'Your store pickup order has been received! We will contact you soon.')
            
        elif order_type == 'delivery':
            # Delivery order
            order = Order.objects.create(
                full_name=request.POST.get('full_name'),
                phone_number=request.POST.get('phone_number'),
                email=request.POST.get('email', ''),
                address=request.POST.get('address', ''),
                product=product,
                order_type='delivery',
                notes=request.POST.get('notes', '')
            )
            messages.success(request, 'Your delivery order has been received! We will contact you soon.')
        
        return redirect('store:order_success')
    
    context = {
        'product': product,
    }
    return render(request, 'store/checkout.html', context)


def order_success(request):
    """Order success page"""
    return render(request, 'store/order_success.html')


def about(request):
    """About page"""
    return render(request, 'store/about.html')


def contact(request):
    """Contact page with contact form"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )
        
        messages.success(request, 'Your message has been sent! We will contact you soon.')
        return redirect('store:contact')
    
    return render(request, 'store/contact.html')


def it_support(request):
    """IT Support services page"""
    return render(request, 'store/it_support.html')


def it_support_request(request):
    """IT Support request form"""
    if request.method == 'POST':
        form = ITSupportRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your IT support request has been submitted! We will contact you soon.')
            return redirect('store:it_support_success')
    else:
        form = ITSupportRequestForm()
    
    return render(request, 'store/it_support_request.html', {'form': form})


def it_support_success(request):
    """IT Support request success page"""
    return render(request, 'store/it_support_success.html')

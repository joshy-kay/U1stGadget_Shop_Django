from django.db import models
from django.urls import reverse

# Category model for organizing products
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:category', kwargs={'slug': self.slug})


# Product model for electronics items
class Product(models.Model):
    STOCK_CHOICES = [
        ('in_stock', 'In Stock'),
        ('out_of_stock', 'Out of Stock'),
        ('limited', 'Limited Stock'),
    ]

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    stock_status = models.CharField(max_length=20, choices=STOCK_CHOICES, default='in_stock')
    is_featured = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:product_detail', kwargs={'slug': self.slug})


# Contact message model
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} - {self.created_at.strftime('%Y-%m-%d')}"


# Order model for delivery orders
class Order(models.Model):
    ORDER_TYPE_CHOICES = [
        ('delivery', 'Delivery Order'),
        ('store_pickup', 'Store Pickup'),
    ]

    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_type = models.CharField(max_length=20, choices=ORDER_TYPE_CHOICES, default='delivery')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Order #{self.id} - {self.full_name} - {self.product.name}"


# IT Support Service model
class ITService(models.Model):
    SERVICE_TYPE_CHOICES = [
        ('repair', 'Device Repair'),
        ('maintenance', 'System Maintenance'),
        ('upgrade', 'Hardware Upgrade'),
        ('software', 'Software Installation'),
        ('virus', 'Virus Removal'),
        ('data', 'Data Recovery'),
        ('network', 'Network Setup'),
        ('training', 'IT Training'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Low Priority'),
        ('medium', 'Medium Priority'),
        ('high', 'High Priority'),
        ('urgent', 'Urgent'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    name = models.CharField(max_length=200)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPE_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Base price for the service")
    estimated_hours = models.DecimalField(max_digits=5, decimal_places=2, help_text="Estimated time in hours")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = "IT Service"
        verbose_name_plural = "IT Services"

    def __str__(self):
        return f"{self.name} - {self.get_service_type_display()}"


# IT Support Request model
class ITSupportRequest(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low Priority'),
        ('medium', 'Medium Priority'),
        ('high', 'High Priority'),
        ('urgent', 'Urgent'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    device_type = models.CharField(max_length=100, help_text="e.g., Laptop, Phone, Desktop")
    brand_model = models.CharField(max_length=100, help_text="e.g., Dell XPS 15, iPhone 13")
    service_needed = models.TextField(help_text="Describe the issue or service needed")
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    preferred_date = models.DateField(help_text="Preferred service date")
    preferred_time = models.TimeField(help_text="Preferred service time")
    address = models.TextField(help_text="Service location address")
    notes = models.TextField(blank=True, help_text="Additional notes or special requirements")
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "IT Support Request"
        verbose_name_plural = "IT Support Requests"

    def __str__(self):
        return f"Request #{self.id} - {self.full_name} - {self.device_type}"

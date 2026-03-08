from django.contrib import admin
from .models import Category, Product, ContactMessage, Order


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    ordering = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock_status', 'is_featured', 'date_added']
    list_filter = ['category', 'stock_status', 'is_featured', 'date_added']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['price', 'stock_status', 'is_featured']
    ordering = ['-date_added']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'category', 'description')
        }),
        ('Pricing & Stock', {
            'fields': ('price', 'stock_status', 'is_featured')
        }),
        ('Media', {
            'fields': ('image',)
        }),
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'message']
    ordering = ['-created_at']
    readonly_fields = ['name', 'email', 'message', 'created_at']
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected messages as read"
    
    actions = [mark_as_read]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'product', 'phone_number', 'order_type', 'created_at', 'is_completed']
    list_filter = ['order_type', 'is_completed', 'created_at']
    search_fields = ['full_name', 'phone_number', 'product__name']
    ordering = ['-created_at']
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Customer Information', {
            'fields': ('full_name', 'phone_number', 'email')
        }),
        ('Order Details', {
            'fields': ('product', 'order_type', 'address', 'notes')
        }),
        ('Status', {
            'fields': ('is_completed',)
        }),
        ('Timestamp', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def mark_as_completed(self, request, queryset):
        queryset.update(is_completed=True)
    mark_as_completed.short_description = "Mark selected orders as completed"
    
    actions = [mark_as_completed]

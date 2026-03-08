from django import forms
from .models import ContactMessage, Order, ITSupportRequest


class ContactForm(forms.ModelForm):
    """Contact form for the contact page"""
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email',
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your Message',
                'rows': 5,
                'required': True
            }),
        }


class StorePickupForm(forms.ModelForm):
    """Form for store pickup orders"""
    class Meta:
        model = Order
        fields = ['full_name', 'phone_number', 'notes']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full Name',
                'required': True
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number',
                'required': True
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Additional notes (optional)',
                'rows': 3
            }),
        }


class DeliveryOrderForm(forms.ModelForm):
    """Form for delivery orders"""
    class Meta:
        model = Order
        fields = ['full_name', 'phone_number', 'email', 'address', 'notes']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full Name',
                'required': True
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email Address',
                'required': False
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Delivery Address',
                'rows': 3,
                'required': True
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Additional notes (optional)',
                'rows': 3
            }),
        }


class ITSupportRequestForm(forms.ModelForm):
    """Form for IT support service requests"""
    class Meta:
        model = ITSupportRequest
        fields = ['full_name', 'email', 'phone_number', 'device_type', 'brand_model', 
                  'service_needed', 'priority', 'preferred_date', 'preferred_time', 
                  'address', 'notes']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full Name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email Address',
                'required': True
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number',
                'required': True
            }),
            'device_type': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Laptop, Phone, Desktop',
                'required': True
            }),
            'brand_model': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Dell XPS 15, iPhone 13',
                'required': True
            }),
            'service_needed': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe the issue or service needed...',
                'rows': 4,
                'required': True
            }),
            'priority': forms.Select(attrs={
                'class': 'form-select',
                'required': True
            }),
            'preferred_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'required': True
            }),
            'preferred_time': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time',
                'required': True
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Service location address...',
                'rows': 3,
                'required': True
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Additional notes or special requirements...',
                'rows': 3
            }),
        }

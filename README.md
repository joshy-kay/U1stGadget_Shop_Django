# U1st Gadget & Things - E-commerce Website

A complete beginner-friendly Django e-commerce website for selling electronics, phones, computers, and tech gadgets. Built with Django, Bootstrap 5, and SQLite for easy deployment and management.

## 🛍️ Features

### Main Website
- **Home Page**: Hero banner with featured products and latest arrivals
- **Shop Page**: All products with filtering and pagination
- **Category Pages**: Products organized by categories (phones, laptops, accessories)
- **Product Details**: Detailed product information with images
- **About Page**: Business information and values
- **Contact Page**: Contact form with WhatsApp integration
- **IT Support Page**: Professional IT services and support request system

### Product Management
- Add, edit, and delete products
- Upload product images
- Set prices and descriptions
- Assign categories
- Mark products as featured
- Stock status management

### IT Support Services
- **Device Repair**: Professional repair for laptops, phones, and computers
- **Virus Removal**: Complete malware and virus removal
- **Hardware Upgrades**: RAM, SSD installation, performance improvements
- **Software Installation**: OS setup, software configuration
- **Data Recovery**: Recover lost files from damaged drives
- **Network Setup**: Home and office network configuration
- **IT Training**: Technical training and support
- **Service Requests**: Customer can submit detailed IT support requests
- **Priority Management**: Urgent, High, Medium, Low priority levels
- **Status Tracking**: Pending, In Progress, Completed status

### Checkout System
- **Store Purchase**: Customer visits store to inspect and pay
- **Delivery Order**: Home delivery with customer information form
- No online payment integration required
- Orders saved in database for admin viewing

### Admin Dashboard
- Custom admin interface (not just Django default)
- View total products, orders, and IT support requests
- Manage products, orders, contact messages, and IT requests
- Simple login system (admin/admin123)
- Professional dashboard with statistics and management

### Design Features
- Modern electronics store UI
- Dark + blue tech theme
- Responsive mobile design
- Professional footer on all pages
- Bootstrap 5 styling

## 📋 Requirements

- Python 3.8+
- Django 4.2.7
- Pillow 10.1.0 (for image handling)

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install django pillow
```

### 2. Navigate to Project Directory
```bash
cd U1stGadget_Shop_Django
```

### 3. Set Up Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Admin User
```bash
python manage.py createsuperuser
```
- Username: `admin` (recommended)
- Email: your email
- Password: `admin123` (recommended)

### 5. Run Development Server
```bash
python manage.py runserver
```

### 6. Access the Website
- **Main Website**: http://127.0.0.1:8000
- **Admin Dashboard**: http://127.0.0.1:8000/admin_dashboard/
- **Django Admin**: http://127.0.0.1:8000/admin/

## 📚 Beginner Guide

### How to Add Products

1. **Access Admin Dashboard**
   - Go to http://127.0.0.1:8000/admin_dashboard/
   - Login with username: `admin`, password: `admin123`

2. **Add Categories First**
   - Click "Django Admin" in the top-right menu
   - Go to "Categories" under "STORE"
   - Add categories like "Phones", "Laptops", "Accessories"

3. **Add Products**
   - Go to "Products" under "STORE"
   - Click "Add product"
   - Fill in:
     - **Name**: Product title
     - **Slug**: URL-friendly name (auto-generated)
     - **Description**: Product details
     - **Price**: Product price
     - **Category**: Select from dropdown
     - **Image**: Upload product photo
     - **Stock Status**: In Stock, Out of Stock, or Limited
     - **Featured**: Check to show on homepage

### How to Change Business Information

1. **Change Business Name**
   - Edit `templates/base.html`
   - Find: `U1st Gadget & Things`
   - Replace with your business name

2. **Change WhatsApp Number**
   - Edit `templates/store/contact.html`
   - Find: `+23200000000`
   - Replace with your WhatsApp number
   - Also update in `templates/store/product_detail.html`

3. **Change Contact Information**
   - Edit `templates/store/contact.html`
   - Update phone numbers, email, and address

### How to Edit Prices

1. **Via Admin Dashboard**
   - Go to Admin Dashboard → Products
   - Click "Django Admin" next to a product
   - Edit the price field
   - Click "Save"

2. **Via Django Admin**
   - Go to /admin/
   - Navigate to Products
   - Click on any product to edit

### How to Manage Orders

1. **View Orders**
   - Go to Admin Dashboard → Orders
   - See all customer orders
   - Filter by pending/completed status

2. **Mark Orders as Completed**
   - Click the checkmark button next to pending orders
   - Orders move from "Pending" to "Completed"

### How to View Contact Messages

1. **Access Messages**
   - Go to Admin Dashboard → Messages
   - See all customer inquiries
   - Filter by read/unread status

2. **Mark Messages as Read**
   - Click "Mark Read" button
   - Messages move from "New" to "Read"

## 📁 Project Structure

```
u1stgadget/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── db.sqlite3              # SQLite database
├── u1stgadget/            # Django project settings
│   ├── settings.py         # Main configuration
│   ├── urls.py            # URL routing
│   └── wsgi.py           # WSGI configuration
├── store/                 # Main website app
│   ├── models.py          # Database models
│   ├── views.py           # Website views
│   ├── urls.py            # Store URLs
│   ├── admin.py           # Django admin configuration
│   └── forms.py           # Contact and order forms
├── admin_dashboard/        # Custom admin app
│   ├── views.py           # Admin dashboard views
│   ├── urls.py            # Admin URLs
│   └── templates/         # Admin templates
├── templates/             # HTML templates
│   ├── base.html          # Main template
│   └── store/            # Website pages
├── static/                # CSS, JavaScript, images
│   ├── css/              # Stylesheets
│   └── js/               # JavaScript files
└── media/                 # Uploaded product images
    └── products/          # Product images
```

## 🎨 Customization Guide

### Colors and Theme
- Edit `static/css/style.css` to change colors
- Main theme uses blue gradient: `#667eea` to `#764ba2`
- Admin theme uses professional blue: `#4e73df`

### Adding New Pages
1. Create view in `store/views.py`
2. Add URL in `store/urls.py`
3. Create template in `templates/store/`

### Adding New Fields to Products
1. Edit `store/models.py`
2. Add new field to Product model
3. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Update admin.py to include new field

## 🚀 Deployment Guide

### For Production (Beginner Friendly)

1. **Choose Hosting**
   - PythonAnywhere (recommended for beginners)
   - Heroku
   - DigitalOcean (more advanced)

2. **Basic Deployment Steps**
   - Upload project files to server
   - Install dependencies: `pip install django pillow`
   - Set `DEBUG = False` in `settings.py`
   - Configure `ALLOWED_HOSTS` in `settings.py`
   - Run migrations: `python manage.py migrate`
   - Collect static files: `python manage.py collectstatic`
   - Set up web server (Gunicorn + Nginx recommended)

3. **Security Settings**
   - Change secret key in `settings.py`
   - Use environment variables for sensitive data
   - Set up SSL certificate

## 🔧 Troubleshooting

### Common Issues

1. **"Pillow not installed"**
   ```bash
   pip install pillow
   ```

2. **"ModuleNotFoundError"**
   - Make sure you're in the project directory
   - Install requirements: `pip install -r requirements.txt`

3. **Images not displaying**
   - Check `MEDIA_URL` and `MEDIA_ROOT` in settings.py
   - Ensure media directory exists
   - Run server with `python manage.py runserver`

4. **Admin login not working**
   - Create superuser: `python manage.py createsuperuser`
   - Use correct credentials

5. **CSS/JS not loading**
   - Check `STATIC_URL` in settings.py
   - Run `python manage.py collectstatic` for production

### Getting Help

1. Check Django documentation: https://docs.djangoproject.com/
2. Review error messages in terminal
3. Ensure all dependencies are installed
4. Verify file permissions on media and static folders

## 📞 Support

This project is designed to be beginner-friendly. All code is commented and structured for easy understanding and modification.

### Default Login Credentials
- **Admin Dashboard**: username: `admin`, password: `admin123`
- **Django Admin**: Use your created superuser credentials

## 📄 License

This project is open source and available for commercial use. Developed by JayTechSolution.

## 🔄 Updates

To update the project in the future:
1. Backup your database (`db.sqlite3`)
2. Backup media files (`media/`)
3. Test changes in development first
4. Update code gradually

---

**Happy Selling! 🎉**

If you need help with customization or have questions, feel free to reach out to JayTechSolution.

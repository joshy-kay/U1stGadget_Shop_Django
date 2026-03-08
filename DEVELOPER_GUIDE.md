# Developer Onboarding Guide - U1st Gadget Shop

Welcome to the U1st Gadget Shop Django project! This guide will help you get up to speed quickly.

---

## 📋 Project Overview

**U1st Gadget Shop** is a Django-based e-commerce platform specializing in electronics and gadgets with an integrated IT support services system. The project features:

- A public-facing store for browsing and purchasing products
- An admin dashboard for managing products, orders, and IT support requests
- IT support service request system with priority and status tracking
- Responsive design built with Bootstrap 5
- SQLite database for easy local development

---

## 🛠️ Prerequisites

Before you start, ensure you have:

- **Python 3.8+** installed on your system
- **pip** (Python package manager)
- **Git** (for version control)
- A code editor (VS Code recommended)
- Terminal/PowerShell access

Check your Python installation:
```bash
python --version
```

---

## ⚡ Quick Setup (5 minutes)

### 1. Clone/Extract the Repository

If you received the project as a ZIP file, extract it. If using Git:
```bash
git clone <repository-url>
cd U1stGadget_Shop_Django
```

### 2. Create and Activate Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv .venv
. .venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

You should see `(.venv)` at the start of your terminal prompt when activated.

### 3. Install Dependencies

```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

**Note:** If Pillow installation fails on Windows:
- Try: `pip install --only-binary=:all: Pillow`
- Or install "Build Tools for Visual Studio" (Desktop development with C++) and retry

### 4. Set Up Database

```bash
python manage.py makemigrations
python manage.py migrate
```

This creates a fresh SQLite database with all tables.

### 5. Create Admin User

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account (example: username `admin`, password `admin123`).

### 6. Run Development Server

```bash
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
```

---

## 🌐 Accessing the Application

Once running, visit:

| Section | URL |
|---------|-----|
| **Main Store** | http://127.0.0.1:8000 |
| **Admin Dashboard** | http://127.0.0.1:8000/admin_dashboard/ |
| **Django Admin** | http://127.0.0.1:8000/admin/ |
| **IT Support** | http://127.0.0.1:8000/it-support/ |

**Default Admin Credentials** (if you used the recommended values above):
- Username: `admin`
- Password: `admin123`

---

## 📁 Project Structure

```
U1stGadget_Shop_Django/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── db.sqlite3               # Database (auto-generated)
│
├── u1stgadget/              # Main project settings
│   ├── settings.py          # Django configuration
│   ├── urls.py              # Root URL routing
│   ├── wsgi.py              # WSGI server config
│   └── asgi.py              # ASGI server config
│
├── store/                   # Main e-commerce app
│   ├── models.py            # Product, Order, Category models
│   ├── views.py             # Store views (home, shop, checkout)
│   ├── urls.py              # Store URL routes
│   ├── forms.py             # Store forms (OrderForm, etc.)
│   ├── admin.py             # Django admin config
│   └── management/
│       └── commands/
│           └── seed_gadgets.py  # Command to populate sample products
│
├── admin_dashboard/         # Custom admin interface
│   ├── views.py             # Dashboard views
│   ├── urls.py              # Dashboard routes
│   └── templates/
│       ├── login.html
│       ├── dashboard.html
│       ├── products.html
│       ├── orders.html
│       └── ...
│       
├── templates/               # HTML templates
│   ├── base.html            # Base template
│   ├── store/               # Store templates
│   │   ├── home.html
│   │   ├── shop.html
│   │   ├── product_detail.html
│   │   ├── checkout.html
│   │   └── ...
│   └── admin_dashboard/     # Dashboard templates
│
├── static/                  # Static files (CSS, JS, images)
│   ├── css/
│   │   ├── style.css        # Main styling
│   │   └── admin-style.css  # Dashboard styling
│   └── js/
│       ├── script.js
│       └── admin-script.js
│
└── media/                   # User-uploaded files
    └── products/            # Product images
```

---

## 🔑 Key Models

### `store/models.py`

**Category**
- Represents product categories (Phones, Laptops, Accessories)
- Fields: name, description, slug

**Product**
- Represents individual gadgets/products
- Fields: title, description, price, image, category, featured, stock_available
- Related to: Category

**Order**
- Stores customer orders
- Fields: customer_name, customer_email, phone, delivery_type, address, created_at, status
- Related to: Product (M2M through OrderItem)

**OrderItem**
- Junction model linking Order to Product with quantity
- Fields: order (FK), product (FK), quantity

**ITSupportRequest**
- Customer IT support service requests
- Fields: customer_name, email, phone, service_type, priority, status, description, created_at
- Service types: Device Repair, Virus Removal, Hardware Upgrades, etc.

---

## 👀 Apps Overview

### `store` App
Handles the main e-commerce functionality:
- Product catalog and browsing
- Order management (checkout)
- Order placement and tracking
- IT support request submission

**Key Views:**
- `home()` - Landing page with featured products
- `shop()` - All products with filtering
- `product_detail()` - Single product page
- `checkout()` - Order form and processing
- `it_support()` - IT support request form

### `admin_dashboard` App
Custom admin interface for staff:
- Dashboard overview (product count, order count, requests count)
- Product management (add, edit, delete)
- Order viewing and status updates
- IT support request management
- Basic authentication (login required)

**Protected with:** Simple session-based login at `/admin_dashboard/login/`

---

## 🔧 Common Development Tasks

### Adding a New Product Programmatically

```python
from store.models import Category, Product

category = Category.objects.get(name="Phones")
product = Product.objects.create(
    title="Latest Smartphone",
    description="A great phone",
    price=699.99,
    category=category,
    stock_available=50
)
```

### Seeding Sample Products

```bash
python manage.py seed_gadgets
```

This populates the database with sample gadgets and categories.

### Creating Django Migrations

After modifying models:

```bash
python manage.py makemigrations        # Create migration files
python manage.py migrate               # Apply migrations to database
```

### Accessing Django Shell

```bash
python manage.py shell
```

Useful for testing queries and debugging.

### Running Management Commands

```bash
python manage.py <command> <options>
```

---

## 🗄️ Database Operations

### Reset Database (WARNING: Deletes all data)

```bash
# Delete the database file
rm db.sqlite3  # or delete db.sqlite3 manually on Windows

# Recreate it
python manage.py migrate

# Create new superuser
python manage.py createsuperuser
```

### View Database Records

Use Django shell or Django admin:
- Django Admin: http://127.0.0.1:8000/admin/
- Admin Dashboard: http://127.0.0.1:8000/admin_dashboard/

### Backup Database

```bash
# Copy db.sqlite3 to a safe location
cp db.sqlite3 db-backup-$(date +%Y%m%d).sqlite3
```

---

## 🐛 Troubleshooting

### Virtual Environment Not Activating

**Windows PowerShell:**
If you get an execution policy error, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try activation again.

### Pillow Installation Fails

```bash
pip install --only-binary=:all: Pillow
```

Or install MS Build Tools and try again.

### Port 8000 Already in Use

```bash
# Use a different port
python manage.py runserver 8001
```

### Module Not Found Errors

Ensure your virtual environment is activated:
```bash
# Windows
. .venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate
```

Then reinstall dependencies:
```bash
pip install -r requirements.txt
```

### Database Locked Error

If the database is locked by another process:
1. Stop the development server (Ctrl+C)
2. Try again

### Templates Not Loading

Ensure `DEBUG = True` in `u1stgadget/settings.py` for development.

---

## 📝 Development Workflow

### Before Starting Work

1. Activate virtual environment
2. Pull latest code from repository (if using Git)
3. Run migrations: `python manage.py migrate`
4. Start development server: `python manage.py runserver`

### Making Changes

1. Edit files in your editor
2. Django auto-reloads on save (in most cases)
3. Refresh browser to see changes
4. Use browser developer tools (F12) to debug frontend

### Testing Your Changes

1. Navigate to affected URLs
2. Test all user flows
3. Check Django console for errors
4. Use Django shell for database testing

### Committing Code

```bash
git add .
git commit -m "Description of changes"
git push origin main
```

---

## 🚀 Deployment Notes

### Environment Variables

For production, use environment variables instead of hardcoding secrets:

```python
import os
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'fallback-key')
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'
```

Create a `.env` file (keep out of version control):
```
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_DEBUG=False
```

### Production Settings

- Set `DEBUG = False`
- Set `ALLOWED_HOSTS` to your domain(s)
- Use a production database (PostgreSQL recommended)
- Set secure cookie flags
- Enable CSRF protection properly

See `README_DEPLOY.md` for full deployment guide.

---

## 📚 Useful Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Models](https://docs.djangoproject.com/en/4.2/topics/db/models/)
- [Django Views](https://docs.djangoproject.com/en/4.2/topics/http/views/)
- [Bootstrap 5](https://getbootstrap.com/docs/5.0/)

---

## ❓ Questions?

If you encounter issues or have questions:

1. Check the troubleshooting section
2. Review existing issues/PRs in the repository
3. Check Django's official documentation
4. Ask senior developers on the team

---

## ✅ You're Ready!

You should now be able to:
- ✅ Run the development server
- ✅ Navigate the admin dashboard
- ✅ Add/edit products and orders
- ✅ Understand the project structure
- ✅ Make code changes and test them

**Happy coding!** 🎉


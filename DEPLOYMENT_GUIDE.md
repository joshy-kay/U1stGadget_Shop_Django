# 🚀 Django Deployment Checklist

## ✅ Pre-Deployment Steps (Local)

### 1. Verify Project Files
- [ ] `requirements.txt` exists with all dependencies
- [ ] `Procfile` exists for web server
- [ ] `render.yaml` exists for Render deployment
- [ ] Static files are configured in settings.py
- [ ] `DEBUG = False` in production
- [ ] `ALLOWED_HOSTS = ['*']` for demo (restrict later)

### 2. Test Locally First
```bash
# Activate your virtual environment
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Test server locally
python manage.py runserver
```

### 3. Create Git Repository
```bash
git init
git add .
git commit -m "Ready for deployment"
```

---

## 🌐 Hosting Options (Choose One)

### Option A: Render (Recommended - Free Tier Available)
1. Go to https://render.com
2. Sign up/Login with GitHub
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Configure:
   - **Name**: u1st-gadget-shop
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - **Start Command**: `gunicorn u1stgadget.wsgi --bind 0.0.0.0:$PORT`
6. Add Environment Variables:
   - `DJANGO_SETTINGS_MODULE=u1stgadget.settings`
   - `DJANGO_SECRET_KEY` (generate a random string)
   - `DJANGO_DEBUG=False`
7. Click "Create Web Service"

### Option B: Railway (Also Free Tier)
1. Go to https://railway.app
2. Sign up/Login
3. Click "New Project" → "Deploy from GitHub repo"
4. Connect repository
5. Railway auto-detects Django and configures automatically
6. Add environment variables in Railway dashboard

### Option C: PythonAnywhere (Manual Setup)
1. Go to https://pythonanywhere.com
2. Sign up for free account
3. Upload your project files
4. Configure web app manually

---

## 🔧 Post-Deployment Configuration

### 1. Update ALLOWED_HOSTS
After deployment, update `u1stgadget/settings.py`:
```python
ALLOWED_HOSTS = ['your-render-app.onrender.com', 'localhost', '127.0.0.1']
```

### 2. Create Admin User on Live Site
```bash
# SSH into your server or use railway/render console
python manage.py createsuperuser
```

### 3. Seed Sample Data (Optional)
```bash
python manage.py seed_gadgets
```

---

## 📋 Demo URLs Structure

Once deployed, your site will be available at:
- **Main Store**: https://your-app-name.onrender.com/
- **Admin Dashboard**: https://your-app-name.onrender.com/admin_dashboard/
- **Django Admin**: https://your-app-name.onrender.com/admin/

**Default Login**: admin / admin123 (change this!)

---

## 🐛 Troubleshooting

### Build Fails
- Check `requirements.txt` has correct versions
- Ensure all dependencies are listed
- Check for Python version compatibility

### Static Files Not Loading
- Verify `STATIC_ROOT` and `STATIC_URL` in settings.py
- Run `collectstatic` during build
- Check WhiteNoise configuration

### Database Issues
- Run migrations during build process
- Check database URL if using PostgreSQL

### 500 Errors
- Check Django logs in hosting platform
- Verify `SECRET_KEY` is set
- Ensure `DEBUG=False` for production

---

## 📞 Need Help?

If you encounter issues:
1. Check the hosting platform's logs
2. Verify all environment variables are set
3. Test locally with `DEBUG=False`
4. Refer to Django deployment documentation

---

## 🎯 Quick Deploy Commands (After Git Setup)

```bash
# Commit changes
git add .
git commit -m "Deployment ready"
git push origin main

# Then deploy via your chosen platform's dashboard
```

**Ready to deploy! Choose your hosting platform above.** 🚀
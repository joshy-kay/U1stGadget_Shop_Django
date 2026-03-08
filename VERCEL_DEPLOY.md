# 🚀 Deploy Django to Vercel

## 📋 Prerequisites

- Vercel account (sign up at https://vercel.com)
- GitHub account (for connecting repository)

## ⚡ Quick Deploy Steps

### 1. Push Code to GitHub

```bash
# Initialize git if not already done
git init
git add .
git commit -m "Deploy to Vercel"

# Create GitHub repository and push
# (Replace with your GitHub username/repo)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### 2. Deploy on Vercel

1. **Go to Vercel Dashboard**: https://vercel.com/dashboard
2. **Click "New Project"**
3. **Import Git Repository**: Connect your GitHub repo
4. **Configure Project**:
   - **Framework Preset**: Other
   - **Root Directory**: `./` (leave default)
   - **Build Command**: Leave empty (uses Dockerfile)
   - **Output Directory**: Leave empty

### 3. Set Environment Variables

In Vercel dashboard, go to your project → Settings → Environment Variables:

```
DJANGO_SETTINGS_MODULE = u1stgadget.settings
DJANGO_DEBUG = false
DJANGO_SECRET_KEY = your-super-secret-key-here-32-chars-min
```

**Generate a secure SECRET_KEY:**
```python
# Run this locally to generate a key
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### 4. Deploy

Click **"Deploy"** - Vercel will build using the Dockerfile and deploy automatically.

## 🌐 Your Live Site

After deployment, you'll get a URL like:
- `https://your-project-name.vercel.app`

**Test URLs:**
- Main Store: `https://your-project-name.vercel.app/`
- Admin Dashboard: `https://your-project-name.vercel.app/admin_dashboard/`
- Django Admin: `https://your-project-name.vercel.app/admin/`

## 🔧 Post-Deployment Setup

### Create Admin User

You'll need to create an admin user on the live site. Since Vercel doesn't provide SSH access, you have a few options:

**Option A: Use Railway/Render for Database Management**
- Deploy to Railway first just for database setup
- Export the SQLite database
- Import it to Vercel deployment

**Option B: Add Management Command**
I've added a management command for you. After deployment, you can run it via Vercel CLI:

```bash
# Install Vercel CLI
npm install -g vercel

# Login
vercel login

# Run management command
vercel env pull .env.local
python manage.py setup_admin
```

### Seed Sample Data

```bash
# Run via Vercel CLI after deployment
vercel env pull .env.local
python manage.py seed_gadgets
```

## 📁 Files Created for Vercel

- **`Dockerfile`** - Container configuration for Django
- **`vercel.json`** - Vercel deployment configuration
- **`requirements.txt`** - Python dependencies (already existed)

## 🐛 Troubleshooting

### Build Fails
- Check Vercel build logs
- Ensure all dependencies are in `requirements.txt`
- Verify Dockerfile syntax

### Static Files Not Loading
- Check `STATIC_ROOT` and `STATIC_URL` in settings.py
- Dockerfile runs `collectstatic` during build

### Database Issues
- SQLite works but data persists only during build
- For persistent data, consider PostgreSQL add-on

### 500 Errors
- Check Django logs in Vercel dashboard
- Verify environment variables are set
- Ensure `SECRET_KEY` is properly set

## 💡 Vercel Limitations for Django

⚠️ **Important Notes:**
- Vercel is optimized for frontend/serverless, not full Django apps
- Cold starts may be slow (10-30 seconds)
- File uploads to `media/` folder won't persist
- Database is read-only after build
- Consider **Render** or **Railway** for better Django support

## 🔄 Redeploy After Changes

```bash
git add .
git commit -m "Your changes"
git push origin main
```

Vercel will auto-redeploy when you push to main branch.

---

## 🎯 Alternative: Render (Recommended for Django)

If Vercel proves challenging, I recommend **Render** instead:

1. Go to https://render.com
2. Connect GitHub repo
3. Choose "Web Service" → Python
4. Auto-detects Django and configures automatically
5. Better for full Django applications

**Need help with Render instead?** Just let me know!

---

**Ready to deploy!** 🚀 Push to GitHub and import to Vercel.
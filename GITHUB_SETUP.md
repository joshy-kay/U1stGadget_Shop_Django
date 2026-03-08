# 🐙 GitHub Setup Guide for Django Deployment

## 📋 Prerequisites

- GitHub account (create one at https://github.com if you don't have it)
- Git installed on your computer

## ⚡ Step-by-Step GitHub Setup

### Step 1: Install Git (Manual Installation)

Since automated installation failed, let's do it manually:

1. **Download Git**: Go to https://git-scm.com/download/win
2. **Run the installer** (.exe file)
3. **Installation options**:
   - ✅ Use default settings for most options
   - ✅ Choose "Git from the command line and also from 3rd-party software"
   - ✅ Use Windows' default console window
   - ✅ Use MinTTY (the default terminal)
   - ✅ Checkout as-is, commit as-is
   - ✅ Use Windows-style line endings
   - ✅ Use MinTTY (default)
   - ✅ Enable file system caching
   - ✅ Enable Git Credential Manager

4. **After installation**: Close and reopen PowerShell/VS Code

### Step 2: Verify Git Installation

Open PowerShell and run:
```powershell
git --version
```

You should see: `git version 2.x.x.windows.x`

### Step 3: Configure Git

```powershell
# Set your name and email (replace with your info)
git config --global user.name "Your Full Name"
git config --global user.email "your.email@example.com"

# Verify configuration
git config --global --list
```

### Step 4: Initialize Git Repository

```powershell
# Navigate to your project folder
cd C:\Users\JayTech\Desktop\U1stGadget_Shop_Django

# Initialize Git repository
git init

# Add all files to Git
git add .

# Commit the files
git commit -m "Initial commit: U1st Gadget Shop Django project"
```

### Step 5: Create GitHub Repository

1. **Go to GitHub**: https://github.com
2. **Click "New repository"** (green button)
3. **Repository settings**:
   - **Repository name**: `u1st-gadget-shop` or `U1stGadget_Shop_Django`
   - **Description**: `Django e-commerce website for gadgets and IT services`
   - **Visibility**: Public (so Vercel can access it)
   - ❌ **Don't initialize** with README, .gitignore, or license (we already have these)

4. **Click "Create repository"**

### Step 6: Connect Local Repository to GitHub

After creating the repository, GitHub will show you commands. Copy and run them:

```powershell
# Add the remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/u1st-gadget-shop.git

# Push your code to GitHub
git push -u origin main
```

**Example with real username:**
```powershell
git remote add origin https://github.com/johndoe/u1st-gadget-shop.git
git push -u origin main
```

### Step 7: Verify Upload

1. **Go back to GitHub** in your browser
2. **Refresh the repository page**
3. **You should see all your Django files uploaded**

## 🚀 Deploy to Vercel

Once your code is on GitHub:

1. **Go to Vercel**: https://vercel.com
2. **Sign in** with your GitHub account
3. **Click "New Project"**
4. **Import your repository**: `YOUR_USERNAME/u1st-gadget-shop`
5. **Configure**:
   - **Framework Preset**: Python
   - **Root Directory**: `./`
   - **Build Command**: `pip install -r requirements.txt`
   - **Output Directory**: Leave empty
6. **Add Environment Variables**:
   ```
   DJANGO_SETTINGS_MODULE = u1stgadget.settings
   DJANGO_DEBUG = false
   DJANGO_SECRET_KEY = your-32-character-secret-key-here
   ```
7. **Click "Deploy"**

**Note**: Vercel will automatically detect your `vercel.json` and `api/index.py` files.

## 🔧 Generate SECRET_KEY

Run this command locally to generate a secure key:
```powershell
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

Or use an online generator: https://djecrety.ir/

## 📝 Making Changes

After deployment, to update your site:

```powershell
# Make your changes in VS Code
# Then commit and push
git add .
git commit -m "Description of changes"
git push origin main

# Vercel will auto-redeploy
```

## 🐛 Troubleshooting

### Git Commands Not Working
- Make sure Git is installed and PowerShell is restarted
- Try using Git Bash instead of PowerShell

### Push Fails
```powershell
# If you get authentication errors, use Personal Access Token
# Go to GitHub → Settings → Developer settings → Personal access tokens
# Create a new token with repo permissions
# Use it as password when pushing
```

### Repository Not Found
- Double-check the repository name and your GitHub username
- Make sure the repository is public

### Vercel Build Fails
- Check Vercel build logs
- Ensure all files are committed to GitHub
- Verify environment variables are set correctly

## 📞 Need Help?

If you get stuck at any step:

1. **Check the exact error message**
2. **Google the error** + "GitHub" or "Vercel"
3. **Try Git Bash** instead of PowerShell if commands fail
4. **Verify all file paths** are correct

**Your repository URL will be:** `https://github.com/YOUR_USERNAME/u1st-gadget-shop`

**Ready to start?** Follow Step 1 above! 🚀
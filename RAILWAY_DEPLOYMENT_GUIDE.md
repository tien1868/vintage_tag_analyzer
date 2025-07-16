# Railway Deployment Guide

## 🚀 Quick Fix for Template Error

The app now has a **fallback HTML** that will work even if templates fail to load. This should resolve the `TemplateNotFound` error.

## 📋 Deployment Checklist

### 1. Verify GitHub Repository
- ✅ Repository: `https://github.com/tien1868/vintage_tag_analyzer`
- ✅ All files committed and pushed
- ✅ Templates folder included
- ✅ Fallback HTML implemented

### 2. Railway Setup
1. Go to [Railway Dashboard](https://railway.app/dashboard)
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Choose your repository: `tien1868/vintage_tag_analyzer`
5. Click "Deploy"

### 3. Environment Variables
Add these in Railway dashboard:
```
OPENAI_API_KEY=your_openai_key_here
XAI_API_KEY=your_xai_key_here
FLASK_ENV=production
```

### 4. Check Deployment Files
Ensure these files are in your repository:
- ✅ `app.py` (main Flask app)
- ✅ `requirements.txt` (dependencies)
- ✅ `Procfile` (deployment command)
- ✅ `runtime.txt` (Python version)
- ✅ `railway.json` (Railway config)
- ✅ `templates/index.html` (template file)

### 5. Manual Deployment Steps

If automatic deployment isn't working:

1. **Clone fresh repository:**
   ```bash
   git clone https://github.com/tien1868/vintage_tag_analyzer.git
   cd vintage_tag_analyzer
   ```

2. **Verify files:**
   ```bash
   ls -la
   # Should show: app.py, requirements.txt, Procfile, templates/
   ```

3. **Test locally:**
   ```bash
   pip install -r requirements.txt
   python app.py
   ```

4. **Push to Railway:**
   - Connect Railway to your GitHub repo
   - Railway will auto-deploy on push

## 🔧 Troubleshooting

### If Railway shows "TemplateNotFound":
- The fallback HTML should handle this
- Check Railway logs for other errors
- Verify all files are in the repository

### If deployment fails:
1. Check Railway logs
2. Verify environment variables
3. Ensure all dependencies are in `requirements.txt`

### If app doesn't start:
1. Check `Procfile` content
2. Verify Python version in `runtime.txt`
3. Check Railway logs for startup errors

## 📱 Testing Your App

Once deployed, your app will be available at:
`https://your-app-name.up.railway.app`

### Test the app:
1. Upload an image
2. Check if analysis works
3. Verify both xAI and OpenAI fallbacks

## 🆘 Still Having Issues?

1. **Check Railway logs** in the dashboard
2. **Verify GitHub connection** in Railway
3. **Test locally first** with `python app.py`
4. **Check environment variables** are set correctly

## ✅ Success Indicators

- ✅ App loads without template errors
- ✅ File upload works
- ✅ Image analysis returns results
- ✅ Both AI providers work (with fallbacks)

---

**Need help?** Check Railway logs and GitHub repository status first! 
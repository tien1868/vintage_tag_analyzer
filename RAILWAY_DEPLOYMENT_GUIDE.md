# Railway Deployment Guide

## 🚀 Quick Deployment Steps

### 1. Test Locally First
```bash
# Test health endpoint
python test_health_local.py

# Test gunicorn
gunicorn --check-config app:app

# Test full startup
gunicorn -b 0.0.0.0:5000 app:app
```

### 2. Push to GitHub
```bash
git add .
git commit -m "Fix Railway deployment - health endpoint and nixpacks config"
git push origin main
```

### 3. Railway Dashboard Setup

#### Environment Variables
Go to your Railway service → Variables and add:
- `OPENAI_API_KEY`: `sk-proj-your-actual-key`
- `XAI_API_KEY`: `xa-your-actual-key` (optional)

#### Health Check Settings
- Service → Settings → Healthcheck
- Path: `/health`
- Timeout: 600s (10 minutes)

## 🔧 Configuration Files

### railway.json
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "nixpacks"
  },
  "deploy": {
    "healthcheckPath": "/health",
    "healthcheckTimeout": 600,
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 5
  }
}
```

### nixpacks.toml
```toml
[phases.setup]
nixPkgs = ["python39", "python39Packages.pip"]

[phases.install]
cmds = ["pip install -r requirements.txt"]

[phases.build]
cmds = ["echo 'Build complete'"]

[start]
cmd = "gunicorn -b 0.0.0.0:$PORT app:app"
```

### Procfile
```
web: gunicorn -b 0.0.0.0:$PORT app:app
```

## 🐛 Troubleshooting

### Health Check Fails
1. **Check logs**: Railway → Deployments → Latest → Logs
2. **Verify health endpoint**: Should return "OK" with 200 status
3. **Test locally**: `curl http://localhost:5000/health`

### Build Fails
1. **Check requirements.txt**: All dependencies listed
2. **Verify Python version**: Using Python 3.9 in nixpacks
3. **Check file structure**: All files committed to git

### App Won't Start
1. **Check Procfile**: Correct gunicorn command
2. **Verify app.py**: Has `if __name__ == '__main__'` block
3. **Test locally**: `gunicorn -b 0.0.0.0:5000 app:app`

### Environment Variables
1. **Check Railway dashboard**: Variables tab
2. **Verify names**: `OPENAI_API_KEY`, `XAI_API_KEY`
3. **Test locally**: Set env vars and run app

## 📊 Monitoring

### Railway Dashboard
- **Deployments**: Check build and deploy status
- **Logs**: Real-time application logs
- **Variables**: Environment variable management
- **Settings**: Health check configuration

### Health Check
- **Path**: `/health`
- **Expected Response**: "OK" with 200 status
- **Timeout**: 600 seconds (10 minutes)

## 🔄 Deployment Process

1. **Push to GitHub**: Triggers automatic deployment
2. **Build Phase**: nixpacks installs dependencies
3. **Deploy Phase**: Starts gunicorn with app
4. **Health Check**: Railway tests `/health` endpoint
5. **Live**: App becomes available at Railway URL

## 🎯 Success Indicators

✅ **Build completes** in ~20-30 seconds  
✅ **Health check passes** on first attempt  
✅ **App responds** to web requests  
✅ **Environment variables** loaded correctly  
✅ **No restart loops** in deployment logs  

## 🚨 Common Issues

### "Service Unavailable"
- Health check failing
- App not starting properly
- Environment variables missing

### "Build Timeout"
- Large dependencies
- Network issues
- Complex build process

### "Port Already in Use"
- Multiple processes
- Wrong port configuration
- Development server conflicts

## 📞 Support

If deployment still fails:
1. Check Railway logs for specific errors
2. Test locally with `python test_health_local.py`
3. Verify all configuration files are correct
4. Ensure environment variables are set in Railway dashboard

## 🎉 Success!

Once deployed successfully:
- Share the Railway URL with your friend
- The app will be available 24/7
- Monitor usage in Railway dashboard
- Add billing if needed for higher usage 
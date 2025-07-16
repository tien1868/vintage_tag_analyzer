# 🔧 Fix Railway Environment Variables

## Current Issue
Your Railway dashboard shows:
- ❌ Variable name: `open_ai_key:` (incorrect)
- ❌ App expects: `OPENAI_API_KEY` (correct)

## How to Fix

### 1. Update Railway Variables
In your Railway dashboard:

1. **Go to Variables tab**
2. **Delete the current variable** `open_ai_key:`
3. **Add these correct variables:**

```
OPENAI_API_KEY=your_openai_api_key_here
XAI_API_KEY=your_xai_api_key_here
FLASK_ENV=production
```

### 2. Variable Names Must Match
- ✅ `OPENAI_API_KEY` (not `open_ai_key:`)
- ✅ `XAI_API_KEY` (not `xai_api_key`)
- ✅ `FLASK_ENV=production`

### 3. After Updating Variables
1. **Redeploy** your app in Railway
2. **Check logs** for any errors
3. **Test the app** with an image upload

## Expected Result
After fixing the variables, your app should:
- ✅ Load without template errors
- ✅ Accept image uploads
- ✅ Use real AI analysis (not demo)
- ✅ Show "OpenAI" or "xAI" as provider

## Troubleshooting
If it still doesn't work:
1. Check Railway logs for API errors
2. Verify API keys are valid
3. Test locally with `python app.py`

---

**The key issue:** Railway variable names must exactly match what the app expects! 
# 🔑 API Key Setup Guide

## 📋 Overview

This guide will help you set up API keys for the Vintage Tag Analyzer app.

## 🎯 Required API Keys

### 1. OpenAI API Key (Recommended)
- **Purpose**: Primary AI analysis using GPT-4o
- **Cost**: Pay-per-use (very affordable)
- **Setup**: Required for full functionality

### 2. xAI API Key (Optional)
- **Purpose**: Alternative AI analysis using Grok
- **Cost**: Free tier available
- **Setup**: Optional, app works without it

## 🔧 Getting Your API Keys

### OpenAI API Key
1. **Visit**: https://platform.openai.com/account/api-keys
2. **Sign In**: Use your OpenAI account (or create one)
3. **Create Key**: Click "Create new secret key"
4. **Copy Key**: The key starts with `sk-`
5. **Save Securely**: Store it safely (you won't see it again)

### xAI API Key (Optional)
1. **Visit**: https://console.x.ai
2. **Sign Up**: Create an account
3. **Get Key**: Find your API key in the dashboard
4. **Copy Key**: Save it securely

## 🚀 Adding to Railway

### Method 1: Railway Dashboard
1. Go to https://railway.app
2. Select your project
3. Click "Variables" tab
4. Click "New Variable"
5. Add each key:
   - **Name**: `OPENAI_API_KEY`
   - **Value**: `sk-your-key-here`
   - **Name**: `XAI_API_KEY`
   - **Value**: `your-xai-key-here`

### Method 2: Railway CLI
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Add variables
railway variables set OPENAI_API_KEY=sk-your-key-here
railway variables set XAI_API_KEY=your-xai-key-here
```

## 🧪 Testing Your Keys

### Local Testing
```bash
# Set environment variables
export OPENAI_API_KEY="sk-your-key-here"
export XAI_API_KEY="your-xai-key-here"

# Test the keys
python test_api_keys.py
```

### Expected Output
```
🔑 Testing API Keys
==============================
✅ OpenAI API key is valid
✅ xAI API key is valid

📊 Results:
OpenAI: ✅ Valid
xAI: ✅ Valid

🎉 At least one API key is working!
   Your app will function with demo fallback for missing keys.
```

## 💰 Cost Information

### OpenAI Pricing
- **GPT-4o**: ~$0.01 per image analysis
- **Free Tier**: $5 credit monthly
- **Pay-as-you-go**: No monthly fees

### xAI Pricing
- **Free Tier**: Available
- **Paid Plans**: Check console.x.ai for current pricing

## 🔒 Security Best Practices

1. **Never commit API keys to code**
2. **Use environment variables only**
3. **Rotate keys regularly**
4. **Monitor usage in dashboard**
5. **Set up billing alerts**

## 🚨 Troubleshooting

### Common Issues

**"Invalid API key"**
- Check key format (OpenAI starts with `sk-`)
- Verify key is copied correctly
- Ensure no extra spaces

**"Rate limit exceeded"**
- Wait a few minutes
- Check your usage limits
- Consider upgrading plan

**"Payment required"**
- Add billing information
- Check account status
- Verify payment method

### Testing Commands

```bash
# Test OpenAI
curl -H "Authorization: Bearer sk-your-key" https://api.openai.com/v1/models

# Test xAI
curl -X POST https://api.x.ai/v1/chat/completions \
  -H "Authorization: Bearer your-xai-key" \
  -H "Content-Type: application/json" \
  -d '{"model":"grok-1","messages":[{"role":"user","content":"Hello"}],"max_tokens":10}'
```

## 📞 Support

- **OpenAI**: https://help.openai.com
- **xAI**: https://console.x.ai/support
- **Railway**: https://railway.app/docs

## ✅ Checklist

- [ ] Get OpenAI API key
- [ ] Get xAI API key (optional)
- [ ] Add to Railway Variables
- [ ] Test keys locally
- [ ] Deploy to Railway
- [ ] Test app functionality
- [ ] Monitor usage and costs 
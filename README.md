# 🎯 Vintage Tag Analyzer

AI-powered web application for analyzing military and vintage tags using xAI and OpenAI APIs.

## 🚀 Features

- **Image Analysis**: Upload images of military/vintage tags
- **AI-Powered**: Uses xAI Grok and OpenAI GPT-4o for analysis
- **Text Extraction**: Extracts text from images
- **Age Estimation**: Estimates item age and historical context
- **Market Value**: Provides current market value assessment
- **Fallback System**: Demo analysis when APIs are unavailable
- **Modern UI**: Clean, responsive web interface

## 🛠️ Local Development

### Prerequisites
- Python 3.11+
- Flask
- Requests

### Installation
```bash
# Clone the repository
git clone <your-repo-url>
cd vintage_tag_analyzer

# Install dependencies
pip install -r requirements.txt

# Set environment variables (optional for local testing)
export OPENAI_API_KEY="your-openai-key"
export XAI_API_KEY="your-xai-key"

# Run the application
python app.py
```

### Local Testing
1. Open http://localhost:5000
2. Upload an image of a vintage tag
3. View AI analysis results

## 🚀 Deployment on Railway

### 1. Prepare Your Repository
Ensure your code is pushed to GitHub with these files:
- `app.py` - Main Flask application
- `requirements.txt` - Python dependencies
- `Procfile` - Railway process definition
- `railway.json` - Railway configuration
- `templates/` - HTML templates

### 2. Create Railway Project
1. Go to [Railway.app](https://railway.app)
2. Sign in with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository

### 3. Configure Environment Variables
In Railway dashboard, add these variables:
- `OPENAI_API_KEY`: Your OpenAI API key (from https://platform.openai.com/account/api-keys)
- `XAI_API_KEY`: Your xAI API key (optional, from https://console.x.ai)

### 4. Deploy
Railway will automatically:
- Detect Python project
- Install dependencies from `requirements.txt`
- Use Gunicorn for production serving
- Bind to Railway's `$PORT` environment variable
- Start the application

### 5. Access Your App
- Railway provides a URL like: `https://your-app.up.railway.app`
- The app will be available immediately after successful deployment

## 📁 Project Structure

```
vintage_tag_analyzer/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Procfile           # Railway process definition
├── railway.json       # Railway configuration
├── wsgi.py           # WSGI entry point (backup)
├── templates/         # HTML templates
│   └── index.html    # Main web interface
└── uploads/          # Temporary file storage
```

## 🔧 Configuration Files

### requirements.txt
```
Flask==2.3.3
requests==2.31.0
gunicorn>=20.1.0
```

### Procfile
```
web: gunicorn -b 0.0.0.0:$PORT app:app
```

### railway.json
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "nixpacks"
  },
  "deploy": {
    "healthcheckPath": "/health",
    "healthcheckTimeout": 300,
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

## 🚨 Troubleshooting

### Common Issues

1. **Build Fails**
   - Check `requirements.txt` for correct dependencies
   - Ensure all files are committed to GitHub
   - Check Railway build logs for specific errors

2. **Health Check Fails**
   - Verify `/health` endpoint returns `{"status": "healthy"}`
   - Check if app starts properly in Railway logs
   - Ensure port binding uses `$PORT` environment variable

3. **API Key Issues**
   - Set environment variables in Railway dashboard
   - Verify API keys are valid and have sufficient credits
   - Check API rate limits

4. **File Upload Issues**
   - Ensure `uploads/` directory exists
   - Check file size limits (16MB max)
   - Verify file permissions

### Railway Logs
- View build logs in Railway dashboard
- Check deployment logs for startup issues
- Monitor application logs for runtime errors

## 🔒 Security Notes

- API keys are stored as environment variables (not in code)
- File uploads are temporary and deleted on restart
- Debug mode is disabled in production
- HTTPS is automatically provided by Railway

## 📈 Monitoring

Railway provides:
- Real-time logs
- Performance metrics
- Automatic restarts on failure
- Health check monitoring

## 🎯 API Endpoints

- `GET /` - Main web interface
- `POST /analyze` - Image analysis endpoint
- `GET /health` - Health check endpoint
- `GET /uploads/<filename>` - Serve uploaded files

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally with `python app.py`
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.


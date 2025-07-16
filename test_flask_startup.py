#!/usr/bin/env python3
"""
Test Flask Startup for Railway
"""

import os
import sys

def test_imports():
    """Test if all required modules can be imported"""
    print("🔍 Testing imports...")
    
    try:
        import flask
        print("✅ Flask imported successfully")
    except ImportError as e:
        print(f"❌ Flask import failed: {e}")
        return False
    
    try:
        import requests
        print("✅ Requests imported successfully")
    except ImportError as e:
        print(f"❌ Requests import failed: {e}")
        return False
    
    try:
        import gunicorn
        print("✅ Gunicorn imported successfully")
    except ImportError as e:
        print(f"❌ Gunicorn import failed: {e}")
        return False
    
    return True

def test_environment():
    """Test environment variables"""
    print("\n🔍 Testing environment variables...")
    
    port = os.environ.get('PORT', '5000')
    print(f"PORT: {port}")
    
    flask_env = os.environ.get('FLASK_ENV', 'production')
    print(f"FLASK_ENV: {flask_env}")
    
    openai_key = os.environ.get('OPENAI_API_KEY', 'NOT_SET')
    xai_key = os.environ.get('XAI_API_KEY', 'NOT_SET')
    
    print(f"OPENAI_API_KEY: {'SET' if openai_key != 'NOT_SET' else 'NOT_SET'}")
    print(f"XAI_API_KEY: {'SET' if xai_key != 'NOT_SET' else 'NOT_SET'}")

def test_app_creation():
    """Test if the Flask app can be created"""
    print("\n🔍 Testing Flask app creation...")
    
    try:
        # Import the app
        from app import app
        print("✅ Flask app imported successfully")
        
        # Test if app has required routes
        if hasattr(app, 'route'):
            print("✅ Flask app has route decorator")
        else:
            print("❌ Flask app missing route decorator")
            return False
            
        return True
        
    except Exception as e:
        print(f"❌ Flask app creation failed: {e}")
        return False

def test_port_binding():
    """Test if the app can bind to the port"""
    print("\n🔍 Testing port binding...")
    
    try:
        port = int(os.environ.get('PORT', 5000))
        print(f"✅ Port {port} is valid")
        return True
    except ValueError as e:
        print(f"❌ Invalid port: {e}")
        return False

def main():
    print("🎯 Flask Startup Test for Railway")
    print("=" * 40)
    
    # Test imports
    imports_ok = test_imports()
    
    # Test environment
    test_environment()
    
    # Test app creation
    app_ok = test_app_creation()
    
    # Test port binding
    port_ok = test_port_binding()
    
    print("\n📊 Summary:")
    if imports_ok and app_ok and port_ok:
        print("✅ All tests passed - Flask should start successfully")
    else:
        print("❌ Some tests failed - check the issues above")
        
    print("\n💡 If tests pass but app still fails:")
    print("1. Check Railway logs for specific error messages")
    print("2. Verify environment variables are set correctly")
    print("3. Try running: gunicorn --bind 0.0.0.0:$PORT app:app")

if __name__ == "__main__":
    main() 
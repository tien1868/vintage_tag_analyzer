#!/usr/bin/env python3
"""
Test script to verify app health and configuration before deployment.
"""

import sys
import os

# Ensure the app can be imported
try:
    from app import app
    print("✅ Flask app imported successfully.")
except ImportError as e:
    print(f"❌ Failed to import Flask app: {e}")
    print("   Make sure app.py exists and doesn't have syntax errors.")
    sys.exit(1)
except Exception as e:
    print(f"❌ An unexpected error occurred during app import: {e}")
    sys.exit(1)

def test_health_endpoint():
    """Test the health endpoint using Flask's test client."""
    print("\n🧪 Testing health endpoint...")
    try:
        with app.test_client() as client:
            response = client.get('/health')
            
            if response.status_code == 200 and response.data.decode('utf-8').strip() == 'OK':
                print("✅ Health endpoint is working correctly!")
                print(f"   - Status: {response.status_code}")
                print(f"   - Response: '{response.data.decode('utf-8').strip()}'")
                return True
            else:
                print("❌ Health endpoint failed!")
                print(f"   - Status: {response.status_code}")
                print(f"   - Response: '{response.data.decode('utf-8')}'")
                return False
    except Exception as e:
        print(f"❌ An exception occurred while testing the health endpoint: {e}")
        return False

def check_gunicorn_compatibility():
    """Checks for Gunicorn compatibility issues on the current OS."""
    print("\n🧪 Checking Gunicorn compatibility...")
    if sys.platform == "win32":
        print("   - OS: Windows")
        print("   - Gunicorn has limited compatibility on Windows.")
        print("   - The local Gunicorn check will be skipped.")
        print("   - ✅ This is expected and will not affect Railway deployment (which uses Linux).")
        return True # Skip test on windows
    
    # This part will run on non-windows systems
    print("   - OS: Non-Windows")
    try:
        import fcntl
        print("   - ✅ fcntl module is available. Gunicorn should be compatible.")
        return True
    except ImportError:
        print("   - ❌ fcntl module not found. Gunicorn will not work.")
        return False

def main():
    """Run all pre-deployment checks."""
    print("🎯 VINTAGE TAG ANALYZER - DEPLOYMENT CHECK")
    print("=" * 50)
    
    health_ok = test_health_endpoint()
    gunicorn_ok = check_gunicorn_compatibility()
    
    print("\n📊 TEST RESULTS:")
    print(f"   - Health Endpoint: {'✅ PASS' if health_ok else '❌ FAIL'}")
    print(f"   - Gunicorn Check:  {'✅ PASS' if gunicorn_ok else '❌ FAIL'}")
    
    print("-" * 50)
    
    if health_ok and gunicorn_ok:
        print("\n🎉 All checks passed! Your app is ready for Railway.")
        print("   Commit and push your changes to deploy.")
        print("   Command: git push origin main")
    else:
        print("\n⚠️  Some checks failed. Please review the errors above before deploying.")

if __name__ == "__main__":
    main() 
#!/usr/bin/env python3
"""
Test health endpoint locally
"""

import requests
import time

def test_health_endpoint():
    """Test the health endpoint"""
    print("🧪 Testing Health Endpoint")
    print("=" * 30)
    
    try:
        # Start the app in background (you'll need to run this separately)
        print("1. Start the app: python app.py")
        print("2. Then run this test in another terminal")
        print()
        
        # Test the health endpoint
        response = requests.get('http://localhost:5000/health', timeout=5)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        
        if response.status_code == 200:
            print("✅ Health endpoint is working!")
            return True
        else:
            print("❌ Health endpoint failed")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to app")
        print("   Make sure the app is running on http://localhost:5000")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    test_health_endpoint() 
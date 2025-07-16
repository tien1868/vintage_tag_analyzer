#!/usr/bin/env python3
"""
Test API Keys - Verify xAI and OpenAI keys work
"""

import requests
import json

# Your API keys
XAI_API_KEY = os.environ.get('XAI_API_KEY', '')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')

def test_xai_key():
    """Test xAI API key"""
    print("🔍 Testing xAI API key...")
    
    url = "https://api.x.ai/v1/models"
    headers = {
        "Authorization": f"Bearer {XAI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        print(f"📡 xAI Response Status: {response.status_code}")
        
        if response.status_code == 200:
            models = response.json()
            print(f"✅ xAI key valid! Available models: {[m['id'] for m in models.get('data', [])]}")
            return True
        else:
            print(f"❌ xAI key invalid: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ xAI test failed: {e}")
        return False

def test_openai_key():
    """Test OpenAI API key"""
    print("🔍 Testing OpenAI API key...")
    
    url = "https://api.openai.com/v1/models"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        print(f"📡 OpenAI Response Status: {response.status_code}")
        
        if response.status_code == 200:
            models = response.json()
            print(f"✅ OpenAI key valid! Available models: {[m['id'] for m in models.get('data', [])[:5]]}")
            return True
        else:
            print(f"❌ OpenAI key invalid: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ OpenAI test failed: {e}")
        return False

if __name__ == "__main__":
    print("🧪 API KEY TESTER")
    print("=" * 50)
    
    xai_works = test_xai_key()
    print()
    openai_works = test_openai_key()
    
    print("\n" + "=" * 50)
    if xai_works and openai_works:
        print("✅ Both API keys are working!")
    elif xai_works:
        print("✅ xAI key works, ❌ OpenAI key needs fixing")
    elif openai_works:
        print("❌ xAI key needs fixing, ✅ OpenAI key works")
    else:
        print("❌ Both API keys need fixing")
    
    print("=" * 50) 
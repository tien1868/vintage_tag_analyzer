#!/usr/bin/env python3
"""
Test API keys locally before deploying
"""

import os
import requests

def test_openai_key():
    """Test OpenAI API key"""
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        print("❌ OPENAI_API_KEY not found in environment")
        return False
    
    url = "https://api.openai.com/v1/models"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print("✅ OpenAI API key is valid")
            return True
        else:
            print(f"❌ OpenAI API key failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ OpenAI API test failed: {e}")
        return False

def test_xai_key():
    """Test xAI API key"""
    api_key = os.environ.get('XAI_API_KEY')
    if not api_key:
        print("❌ XAI_API_KEY not found in environment")
        return False
    
    url = "https://api.x.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "grok-1",
        "messages": [
            {"role": "user", "content": "Hello"}
        ],
        "max_tokens": 10
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            print("✅ xAI API key is valid")
            return True
        else:
            print(f"❌ xAI API key failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ xAI API test failed: {e}")
        return False

def main():
    print("🔑 Testing API Keys")
    print("=" * 30)
    
    openai_ok = test_openai_key()
    xai_ok = test_xai_key()
    
    print("\n📊 Results:")
    print(f"OpenAI: {'✅ Valid' if openai_ok else '❌ Invalid/Not Set'}")
    print(f"xAI: {'✅ Valid' if xai_ok else '❌ Invalid/Not Set'}")
    
    if openai_ok or xai_ok:
        print("\n🎉 At least one API key is working!")
        print("   Your app will function with demo fallback for missing keys.")
    else:
        print("\n⚠️  No valid API keys found.")
        print("   Your app will use demo analysis only.")

if __name__ == "__main__":
    main() 
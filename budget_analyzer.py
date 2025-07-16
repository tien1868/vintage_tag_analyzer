#!/usr/bin/env python3
"""
Budget Image Analyzer - Uses cheaper OpenAI models for military/vintage tag analysis
"""

import base64
import requests
import json
import sys
import os

# Your OpenAI API key
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')

def encode_image(image_path):
    """Encode image to base64"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def analyze_with_openai(base64_image, model="gpt-4o-mini"):
    """Analyze image with OpenAI (using cheaper model)"""
    url = "https://api.openai.com/v1/chat/completions"
    
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Analyze this image: extract text, identify the item, estimate age, historical context, and current market value. Format with clear sections."},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                ]
            }
        ],
        "max_tokens": 800
    }
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        print(f"🤖 Sending request to OpenAI ({model})...")
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 200:
            result = response.json()["choices"][0]["message"]["content"]
            return result
        elif response.status_code == 429:
            error_data = response.json()
            return f"❌ Rate limit exceeded: {error_data.get('error', {}).get('message', 'Unknown error')}\n\n💡 Try again in a few minutes or check your OpenAI billing."
        elif response.status_code == 401:
            return "❌ Invalid API key. Please check your OpenAI API key."
        elif response.status_code == 402:
            return "❌ Payment required. Please add billing information to your OpenAI account."
        else:
            error_data = response.json()
            return f"❌ API Error ({response.status_code}): {error_data.get('error', {}).get('message', 'Unknown error')}"
            
    except requests.exceptions.Timeout:
        return "❌ Request timed out. Please try again."
    except requests.exceptions.RequestException as e:
        return f"❌ Network error: {e}"
    except Exception as e:
        return f"❌ Unexpected error: {e}"

def check_billing_status():
    """Check OpenAI billing status"""
    url = "https://api.openai.com/v1/dashboard/billing/subscription"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            print(f"💰 Billing Status:")
            print(f"   Plan: {data.get('plan', {}).get('id', 'Unknown')}")
            print(f"   Status: {data.get('status', 'Unknown')}")
            return True
        else:
            print("❌ Could not check billing status")
            return False
    except Exception as e:
        print(f"❌ Error checking billing: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python budget_analyzer.py path/to/image.jpg")
        sys.exit(1)
    
    image_path = sys.argv[1]
    
    if not os.path.exists(image_path):
        print(f"❌ Image not found: {image_path}")
        sys.exit(1)
    
    print("🎯 BUDGET IMAGE ANALYZER")
    print("=" * 50)
    print(f"📸 Analyzing: {image_path}")
    
    # Check billing first
    print("\n💰 Checking billing status...")
    check_billing_status()
    
    # Encode the image
    try:
        base64_image = encode_image(image_path)
        print(f"✅ Image encoded ({len(base64_image)} characters)")
    except Exception as e:
        print(f"❌ Failed to encode image: {e}")
        return
    
    # Try with cheaper model first
    print("\n🤖 Trying with GPT-4o-mini (cheaper)...")
    result = analyze_with_openai(base64_image, "gpt-4o-mini")
    
    if "❌" in result and "quota" in result.lower():
        print("\n🔄 Quota exceeded, trying with demo analysis...")
        from demo_analyzer import create_mock_analysis
        result = create_mock_analysis(image_path)
        result += "\n\n💡 This is a demo analysis. To get real AI analysis:"
        result += "\n   1. Add billing to your OpenAI account"
        result += "\n   2. Try again in a few minutes"
    
    print("\n📊 ANALYSIS RESULT")
    print("=" * 50)
    print(result)

if __name__ == "__main__":
    main() 
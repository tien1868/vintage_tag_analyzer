#!/usr/bin/env python3
"""
OpenAI Image Analyzer - Simplified version for military/vintage tag analysis
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

def analyze_with_openai(base64_image):
    """Analyze image with OpenAI GPT-4o"""
    url = "https://api.openai.com/v1/chat/completions"
    
    payload = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Analyze this image of a military or vintage tag: extract text, identify the item, estimate age, historical context, and current market value. Format your response with clear sections for each analysis."},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                ]
            }
        ],
        "max_tokens": 1000
    }
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        print("🤖 Sending request to OpenAI...")
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

def main():
    if len(sys.argv) < 2:
        print("Usage: python openai_analyzer.py path/to/image.jpg")
        sys.exit(1)
    
    image_path = sys.argv[1]
    
    if not os.path.exists(image_path):
        print(f"❌ Image not found: {image_path}")
        sys.exit(1)
    
    print("🎯 OPENAI IMAGE ANALYZER")
    print("=" * 50)
    print(f"📸 Analyzing: {image_path}")
    
    # Encode the image
    try:
        base64_image = encode_image(image_path)
        print(f"✅ Image encoded ({len(base64_image)} characters)")
    except Exception as e:
        print(f"❌ Failed to encode image: {e}")
        return
    
    # Analyze with OpenAI
    result = analyze_with_openai(base64_image)
    
    print("\n📊 ANALYSIS RESULT")
    print("=" * 50)
    print(result)
    
    if "❌" in result:
        print("\n💡 Troubleshooting:")
        print("   - Check your OpenAI billing at: https://platform.openai.com/account/billing")
        print("   - Try again in a few minutes if rate limited")
        print("   - Use demo_analyzer.py for a mock analysis")

if __name__ == "__main__":
    main() 
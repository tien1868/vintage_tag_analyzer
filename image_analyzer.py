import base64
import requests
import json
import sys

# Replace with your actual API keys
XAI_API_KEY = "your_xai_api_key_here"
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def analyze_with_xai(base64_image):
    url = "https://api.x.ai/v1/chat/completions"  # From xAI docs
    payload = {
        "model": "grok-4",  # Or the vision-capable model
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Analyze this image of a military or vintage tag: extract text, identify the item, estimate age, historical context, and current market value."},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                ]
            }
        ]
    }
    headers = {
        "Authorization": f"Bearer {XAI_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        result = response.json()["choices"][0]["message"]["content"]
        # Simple fallback check: if response indicates low confidence
        if "uncertain" in result.lower() or "not sure" in result.lower():
            print("xAI response uncertain; falling back to OpenAI...")
            return analyze_with_openai(base64_image)
        return result
    else:
        print(f"xAI API error: {response.status_code} - {response.text}")
        return analyze_with_openai(base64_image)  # Fallback on error

def analyze_with_openai(base64_image):
    url = "https://api.openai.com/v1/chat/completions"
    payload = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Analyze this image of a military or vintage tag: extract text, identify the item, estimate age, historical context, and current market value."},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                ]
            }
        ]
    }
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print(f"OpenAI API error: {response.status_code} - {response.text}")
        return "Error analyzing image."

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python image_analyzer.py path/to/image.jpg")
        sys.exit(1)
    
    image_path = sys.argv[1]
    base64_image = encode_image(image_path)
    result = analyze_with_xai(base64_image)
    print("\nAnalysis Result:\n")
    print(result) 
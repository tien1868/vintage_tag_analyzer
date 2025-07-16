#!/usr/bin/env python3
"""
WSGI entry point for Railway deployment
"""

import os
import sys

def main():
    print("🚀 Starting Flask app for Railway...")
    print(f"PORT: {os.environ.get('PORT', '5000')}")
    print(f"Current directory: {os.getcwd()}")
    print(f"Files in directory: {os.listdir('.')}")
    
    try:
        from app import app
        
        port = int(os.environ.get('PORT', 5000))
        print(f"✅ Flask app imported successfully")
        print(f"🎯 Starting server on port {port}")
        
        app.run(host='0.0.0.0', port=port, debug=False)
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        sys.exit(1)
        
    except Exception as e:
        print(f"❌ Startup error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main() 
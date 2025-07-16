#!/usr/bin/env python3
"""
Simple startup script for Railway deployment
"""

import os
import sys

def main():
    print("🚀 Starting Flask app for Railway...")
    
    # Print environment info
    port = os.environ.get('PORT', '5000')
    print(f"PORT: {port}")
    print(f"FLASK_ENV: {os.environ.get('FLASK_ENV', 'production')}")
    
    try:
        # Import and run the Flask app
        from app import app
        
        print("✅ Flask app imported successfully")
        print(f"🎯 Starting server on port {port}")
        
        # Run the app
        app.run(
            host='0.0.0.0',
            port=int(port),
            debug=False
        )
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("💡 Check if all dependencies are installed")
        sys.exit(1)
        
    except Exception as e:
        print(f"❌ Startup error: {e}")
        print("💡 Check Railway logs for more details")
        sys.exit(1)

if __name__ == "__main__":
    main() 
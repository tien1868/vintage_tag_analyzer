#!/usr/bin/env python3
"""
Robust startup script for Railway deployment
"""

import os
import sys
import time

def main():
    print("🚀 Starting Flask app for Railway...")
    
    # Print environment info
    port = os.environ.get('PORT', '5000')
    print(f"PORT: {port}")
    print(f"FLASK_ENV: {os.environ.get('FLASK_ENV', 'production')}")
    print(f"PYTHONPATH: {os.environ.get('PYTHONPATH', 'Not set')}")
    
    # Check if we're in the right directory
    print(f"Current working directory: {os.getcwd()}")
    print(f"Files in current directory: {os.listdir('.')}")
    
    try:
        # Try to import Flask first
        print("🔍 Checking Flask installation...")
        import flask
        print(f"✅ Flask version: {flask.__version__}")
        
        # Try to import our app
        print("🔍 Importing Flask app...")
        from app import app
        
        print("✅ Flask app imported successfully")
        print(f"🎯 Starting server on port {port}")
        
        # Add a small delay to ensure everything is ready
        time.sleep(1)
        
        # Run the app
        app.run(
            host='0.0.0.0',
            port=int(port),
            debug=False,
            threaded=True
        )
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("💡 Check if all dependencies are installed")
        print("💡 Available modules:", [m for m in sys.modules.keys() if 'flask' in m.lower()])
        sys.exit(1)
        
    except Exception as e:
        print(f"❌ Startup error: {e}")
        print("💡 Check Railway logs for more details")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main() 
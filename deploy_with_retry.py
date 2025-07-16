#!/usr/bin/env python3
"""
Railway Deployment with Retry Logic
Handles network issues and build failures
"""

import subprocess
import time
import sys

def run_command_with_retry(command, max_retries=3, delay=5):
    """Run command with retry logic"""
    for attempt in range(max_retries):
        print(f"🔄 Attempt {attempt + 1}/{max_retries}: {command}")
        
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"✅ Command successful: {command}")
                return True
            else:
                print(f"❌ Command failed: {result.stderr}")
                
        except Exception as e:
            print(f"❌ Command error: {e}")
        
        if attempt < max_retries - 1:
            print(f"⏳ Waiting {delay} seconds before retry...")
            time.sleep(delay)
    
    return False

def check_railway_status():
    """Check Railway deployment status"""
    try:
        result = subprocess.run(['railway', 'status'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Railway status check successful")
            print(result.stdout)
            return True
        else:
            print(f"❌ Railway status failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Railway status error: {e}")
        return False

def deploy_with_fallback():
    """Deploy with fallback strategies"""
    print("🚀 Starting Railway deployment with retry logic...")
    
    # Strategy 1: Try with original Dockerfile
    print("\n📦 Strategy 1: Using optimized Dockerfile")
    if run_command_with_retry("git push"):
        print("✅ Push successful with original Dockerfile")
        return True
    
    # Strategy 2: Try with alternative Dockerfile
    print("\n📦 Strategy 2: Using alternative Alpine Dockerfile")
    if run_command_with_retry("cp Dockerfile.alternative Dockerfile"):
        if run_command_with_retry("git add Dockerfile"):
            if run_command_with_retry('git commit -m "Switch to Alpine Dockerfile for better network handling"'):
                if run_command_with_retry("git push"):
                    print("✅ Push successful with Alpine Dockerfile")
                    return True
    
    # Strategy 3: Try Railway CLI deployment
    print("\n📦 Strategy 3: Using Railway CLI")
    if run_command_with_retry("railway login"):
        if run_command_with_retry("railway deploy"):
            print("✅ Railway CLI deployment successful")
            return True
    
    return False

def main():
    print("🎯 Railway Deployment with Retry Logic")
    print("=" * 50)
    
    # Check if we're in a git repository
    if not run_command_with_retry("git status"):
        print("❌ Not in a git repository")
        return
    
    # Try deployment with fallback strategies
    if deploy_with_fallback():
        print("\n🎉 Deployment completed successfully!")
        print("Check your Railway dashboard for the deployment status.")
        
        # Check deployment status
        time.sleep(10)  # Wait for deployment to start
        check_railway_status()
        
    else:
        print("\n❌ All deployment strategies failed.")
        print("Manual intervention required:")
        print("1. Check Railway dashboard for errors")
        print("2. Verify environment variables are set")
        print("3. Try manual deployment from Railway dashboard")

if __name__ == "__main__":
    main() 
#!/usr/bin/env python3
"""
Railway Deployment Helper Script
"""

import os
import subprocess
import sys

def check_railway_cli():
    """Check if Railway CLI is installed"""
    try:
        result = subprocess.run(['railway', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Railway CLI is installed")
            return True
        else:
            print("❌ Railway CLI not found")
            return False
    except FileNotFoundError:
        print("❌ Railway CLI not found")
        return False

def check_git_status():
    """Check git status"""
    try:
        result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
        if result.stdout.strip():
            print("⚠️  You have uncommitted changes:")
            print(result.stdout)
            return False
        else:
            print("✅ Git working directory is clean")
            return True
    except Exception as e:
        print(f"❌ Git error: {e}")
        return False

def deploy_to_railway():
    """Deploy to Railway"""
    print("🚀 Deploying to Railway...")
    
    try:
        # Login to Railway if needed
        result = subprocess.run(['railway', 'login'], capture_output=True, text=True)
        if result.returncode != 0:
            print("❌ Railway login failed")
            return False
        
        # Deploy
        result = subprocess.run(['railway', 'deploy'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Deployment successful!")
            return True
        else:
            print(f"❌ Deployment failed: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Deployment error: {e}")
        return False

def main():
    print("🎯 Railway Deployment Helper")
    print("=" * 40)
    
    # Check prerequisites
    if not check_railway_cli():
        print("\n📦 Install Railway CLI:")
        print("npm install -g @railway/cli")
        return
    
    if not check_git_status():
        print("\n💡 Commit your changes first:")
        print("git add .")
        print("git commit -m 'Your commit message'")
        return
    
    # Deploy
    if deploy_to_railway():
        print("\n🎉 Deployment completed!")
        print("Check your Railway dashboard for the deployment status.")
    else:
        print("\n❌ Deployment failed. Check the logs above.")

if __name__ == "__main__":
    main() 
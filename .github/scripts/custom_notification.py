#!/usr/bin/env python3
"""
Custom notification script for GitHub Actions workflow
This script sends a custom notification to a specified endpoint
"""

import os
import sys
import requests
import json
from datetime import datetime

def send_notification(message, repository, branch):
    """Send notification to custom webhook endpoint"""
    
    webhook_url = os.environ.get('CUSTOM_WEBHOOK_URL')
    api_key = os.environ.get('CUSTOM_API_KEY')
    
    if not webhook_url:
        print("No CUSTOM_WEBHOOK_URL found in environment. Skipping custom notification.")
        return
        
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}' if api_key else ''
    }
    
    payload = {
        'timestamp': datetime.utcnow().isoformat(),
        'message': message,
        'repository': repository,
        'branch': branch,
        'source': 'github-actions'
    }
    
    try:
        response = requests.post(webhook_url, headers=headers, data=json.dumps(payload), timeout=10)
        if response.status_code >= 200 and response.status_code < 300:
            print(f"Custom notification sent successfully: {response.status_code}")
        else:
            print(f"Failed to send custom notification. Status code: {response.status_code}")
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error sending custom notification: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python custom_notification.py <message> <repository> <branch>")
        sys.exit(1)
        
    message = sys.argv[1]
    repository = sys.argv[2]
    branch = sys.argv[3]
    

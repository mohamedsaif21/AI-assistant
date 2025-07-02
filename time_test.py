#!/usr/bin/env python3
"""
Simple script to test the time-based greeting function with Indian Standard Time
"""

from datetime import datetime
import logging
import pytz

def get_time_based_greeting():
    """Get appropriate greeting based on current Indian Standard Time"""
    try:
        # Get current time in Indian Standard Time (IST)
        ist = pytz.timezone('Asia/Kolkata')
        now = datetime.now(ist)
        current_hour = now.hour
        current_time = now.strftime("%I:%M %p")  # Format: 09:40 AM
        current_date = now.strftime("%A, %B %d, %Y")  # Format: Wednesday, July 02, 2025
        
        print(f"Debug: Current IST hour is {current_hour}")
        print(f"Debug: Current IST time is {current_time}")
        print(f"Debug: Current IST date is {current_date}")
        
        # Determine greeting based on Indian time
        if 5 <= current_hour < 12:
            greeting = f"Good morning Mohamed Saif! It's {current_time} IST on {current_date}. I'm Ruhi, your personal assistant. What's the plan for today?"
            time_period = "MORNING"
        elif 12 <= current_hour < 18:
            greeting = f"Good afternoon Mohamed Saif! It's {current_time} IST on {current_date}. I'm Ruhi, your personal assistant. What's the plan for today?"
            time_period = "AFTERNOON"
        elif 18 <= current_hour < 22:
            greeting = f"Good evening Mohamed Saif! It's {current_time} IST on {current_date}. I'm Ruhi, your personal assistant. What's the plan for today?"
            time_period = "EVENING"
        else:
            greeting = f"Good evening Mohamed Saif! It's {current_time} IST on {current_date}. I'm Ruhi, your personal assistant. What's the plan for today?"
            time_period = "NIGHT"
        
        print(f"Debug: Detected time period as {time_period}")
        return greeting
        
    except Exception as e:
        print(f"Error getting current time: {e}")
        return "Hello Mohamed Saif! I'm Ruhi, your personal assistant. What's the plan for today?"

if __name__ == "__main__":
    print("=== INDIAN STANDARD TIME-BASED GREETING TEST ===")
    
    # Show comparison between local time and IST
    local_time = datetime.now()
    ist = pytz.timezone('Asia/Kolkata')
    ist_time = datetime.now(ist)
    
    print(f"Local System Time: {local_time.strftime('%I:%M %p, %A, %B %d, %Y')}")
    print(f"Indian Standard Time: {ist_time.strftime('%I:%M %p, %A, %B %d, %Y')} IST")
    print()
    
    greeting = get_time_based_greeting()
    print("Final Greeting:")
    print(greeting)
    print("\n=== TEST COMPLETE ===")

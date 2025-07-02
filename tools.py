import logging
from livekit.agents import function_tool, RunContext
import requests
from langchain_community.tools import DuckDuckGoSearchRun #<--google search tool free!!
from datetime import datetime
import cv2
import pytz

@function_tool()
async def get_weather(
        context: RunContext, 
        city: str) -> str:
    """
    Get the current weather for a given city.
    """
    try:
        # Try with city name first
        url = f"http://api.wttr.in/{city}?format=%l:+%C+%t+%h+%w+%P"
        response = requests.get(url)
        
        if response.status_code == 200 and "Unknown location" not in response.text:
            logging.info(f"Weather for {city}: {response.text}")
            return response.text.strip()
        
        # Fallback to specific coordinates for known cities
        city_coordinates = {
            "coimbatore": ("11.0013904", "76.9627287"),
            "chennai": ("13.0827", "80.2707"),
            "bangalore": ("12.9716", "77.5946"),
            "mumbai": ("19.0760", "72.8777"),
            "delhi": ("28.7041", "77.1025"),
        }
        
        city_lower = city.lower()
        if city_lower in city_coordinates:
            lat, lon = city_coordinates[city_lower]
            # Try with exact coordinates format that wttr.in expects
            response = requests.get(f"http://api.wttr.in/{lat},{lon}?format=%l:+%C+%t+%h+%w")
            if response.status_code == 200:
                weather_info = response.text.strip()
                logging.info(f"Weather for {city}: {weather_info}")
                return f"Weather in {city}: {weather_info}"
        
        # If still no luck, try simpler format
        response = requests.get(f"http://api.wttr.in/{city}?format=1")
        if response.status_code == 200 and "Unknown location" not in response.text:
            return f"Weather in {city}: {response.text.strip()}"
        
        # Last resort - use web search to get weather
        search_query = f"weather in {city} today current temperature"
        try:
            search_results = DuckDuckGoSearchRun().run(search_query)
            return f"Weather information for {city}: {search_results[:200]}..."
        except:
            pass
        
        logging.error(f"Failed to get weather for {city}")
        return f"Sorry, I couldn't find weather information for {city}. The weather service might not recognize this location."
    except Exception as e:
        logging.error(f"Error getting weather for {city}: {e}")
        return f"An error occurred while retrieving weather for {city}: {str(e)}"

@function_tool()
async def search_web(
        context: RunContext, 
        query: str) -> str:
    """
    Search the web for a given query using DuckDuckGo.
    """
    try:
        results = DuckDuckGoSearchRun().run(query)
        logging.info(f"Search results for '{query}': {results}")
        return results
    except Exception as e:
        logging.error(f"Error searching web for '{query}': {e}")
        return f"An error occurred while searching the web for '{query}'."

@function_tool()
async def get_current_greeting(context: RunContext) -> str:
    """
    Get the current time-appropriate greeting in a friendly but respectful way.
    """
    try:
        current_hour = datetime.now().hour
        
        if 5 <= current_hour < 12:
            return "Good morning, Mohamed! I'm Ruhi, your AI assistant. I hope you're having a wonderful start to your day. How can I help you today?"
        elif 12 <= current_hour < 18:
            return "Good afternoon, Mohamed! It's Ruhi here. I hope your day is going well so far. What can I assist you with?"
        elif 18 <= current_hour < 22:
            return "Good evening, Mohamed! Ruhi at your service. I hope you've had a productive day. How may I help you this evening?"
        else:
            return "Good evening, Mohamed! It's Ruhi here. Working late tonight? I'm here to help with whatever you need."
    except Exception as e:
        logging.error(f"Error getting greeting: {e}")
        return "Hello Mohamed! It's Ruhi, your AI assistant. Great to see you! How can I help you today?"

@function_tool()
async def start_camera_feed(context: RunContext) -> str:
    """
    Start video camera feed using OpenCV with error handling.
    """
    try:
        # Initialize the camera (0 is usually the default camera)
        cap = cv2.VideoCapture(0)
        
        # Check if camera opened successfully
        if not cap.isOpened():
            return "Error: Could not access camera. Please check if camera is connected and not being used by another application."
        
        # Set camera properties (optional)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
        logging.info("Camera feed started successfully")
        
        # Start the video feed loop
        frame_count = 0
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            
            # Check if frame was captured successfully
            if not ret:
                return "Error: Failed to capture frame from camera."
            
            # Display the frame
            cv2.imshow('Camera Feed - Press Q to quit', frame)
            frame_count += 1
            
            # Break the loop on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
            # Optional: Limit to first few frames for demo
            if frame_count > 100:  # Stop after 100 frames for demo
                break
        
        # Release the camera and close windows
        cap.release()
        cv2.destroyAllWindows()
        
        return f"Camera feed completed successfully. Captured {frame_count} frames. Press 'Q' to quit next time."
        
    except cv2.error as cv_error:
        return f"OpenCV Error: {str(cv_error)}. Please check camera drivers and connections."
    except Exception as e:
        logging.error(f"Error in camera feed: {e}")
        return f"Camera access failed: {str(e)}. Please ensure camera permissions are granted."

@function_tool()
async def get_camera_info(context: RunContext) -> str:
    """
    Get information about available cameras and their properties.
    """
    try:
        # Test camera availability
        available_cameras = []
        
        for i in range(3):  # Check first 3 camera indices
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                # Get camera properties
                width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                fps = int(cap.get(cv2.CAP_PROP_FPS))
                
                available_cameras.append(f"Camera {i}: {width}x{height} @ {fps}fps")
                cap.release()
        
        if available_cameras:
            return f"Available cameras found:\n" + "\n".join(available_cameras)
        else:
            return "No cameras detected. Please check camera connections and permissions."
            
    except Exception as e:
        logging.error(f"Error checking cameras: {e}")
        return f"Error checking camera availability: {str(e)}"

# Simple function to get time-based greeting (not a tool)
def get_time_based_greeting():
    """Get appropriate greeting based on current Indian Standard Time"""
    try:
        # Get current time in Indian Standard Time (IST)
        ist = pytz.timezone('Asia/Kolkata')
        now = datetime.now(ist)
        current_hour = now.hour
        current_time = now.strftime("%I:%M %p")  # Format: 09:40 AM
        current_date = now.strftime("%A, %B %d, %Y")  # Format: Wednesday, July 02, 2025
        
        # Determine greeting based on Indian time
        if 5 <= current_hour < 12:
            greeting = f"Good morning Mohamed Saif! It's {current_time} IST on {current_date}. I'm Ruhi, your personal assistant. What's the plan for today?"
        elif 12 <= current_hour < 18:
            greeting = f"Good afternoon Mohamed Saif! It's {current_time} IST on {current_date}. I'm Ruhi, your personal assistant. What's the plan for today?"
        elif 18 <= current_hour < 22:
            greeting = f"Good evening Mohamed Saif! It's {current_time} IST on {current_date}. I'm Ruhi, your personal assistant. What's the plan for today?"
        else:
            greeting = f"Good evening Mohamed Saif! It's {current_time} IST on {current_date}. I'm Ruhi, your personal assistant. What's the plan for today?"
        
        return greeting
        
    except Exception as e:
        logging.error(f"Error getting current time: {e}")
        return "Hello Mohamed Saif! I'm Ruhi, your personal assistant. What's the plan for today?"

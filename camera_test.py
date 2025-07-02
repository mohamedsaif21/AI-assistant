#!/usr/bin/env python3
"""
OpenCV Camera Access Script with Error Handling
Created for Mohamed Saif's AI Project
Inspired by Tony Stark's technology!
"""

import cv2
import sys
import time

def test_camera_access():
    """Test camera access and display video feed"""
    
    print("🎥 Initializing camera system...")
    print("Inspired by Tony Stark's FRIDAY interface!")
    
    try:
        # Initialize the camera (0 is usually the default camera)
        cap = cv2.VideoCapture(0)
        
        # Check if camera opened successfully
        if not cap.isOpened():
            print("❌ Error: Could not access camera!")
            print("   - Check if camera is connected")
            print("   - Ensure no other app is using the camera")
            print("   - Verify camera permissions")
            return False
        
        # Set camera properties for better quality
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        cap.set(cv2.CAP_PROP_FPS, 30)
        
        # Get camera info
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        
        print(f"✅ Camera initialized successfully!")
        print(f"   📐 Resolution: {width}x{height}")
        print(f"   🎬 FPS: {fps}")
        print("\n🚀 Starting video feed...")
        print("💡 Press 'Q' to quit, 'S' to save screenshot")
        
        frame_count = 0
        screenshot_count = 0
        
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            
            # Check if frame was captured successfully
            if not ret:
                print("❌ Error: Failed to capture frame from camera")
                break
            
            frame_count += 1
            
            # Add some information overlay on the frame
            cv2.putText(frame, f"Frame: {frame_count}", (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(frame, "Press 'Q' to quit, 'S' for screenshot", (10, frame.shape[0] - 10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            
            # Display the frame
            cv2.imshow('Mohamed Saif\'s AI Camera Feed', frame)
            
            # Handle key presses
            key = cv2.waitKey(1) & 0xFF
            
            if key == ord('q') or key == ord('Q'):
                print(f"\n🛑 Stopping camera feed. Total frames captured: {frame_count}")
                break
            elif key == ord('s') or key == ord('S'):
                screenshot_count += 1
                filename = f"screenshot_{screenshot_count}.jpg"
                cv2.imwrite(filename, frame)
                print(f"📸 Screenshot saved: {filename}")
        
        # Clean up
        cap.release()
        cv2.destroyAllWindows()
        
        print("✅ Camera feed ended successfully!")
        print(f"📊 Statistics:")
        print(f"   - Total frames: {frame_count}")
        print(f"   - Screenshots: {screenshot_count}")
        
        return True
        
    except cv2.error as cv_error:
        print(f"❌ OpenCV Error: {cv_error}")
        print("   - Check camera drivers")
        print("   - Verify OpenCV installation")
        return False
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def check_available_cameras():
    """Check for available cameras on the system"""
    
    print("🔍 Scanning for available cameras...")
    available_cameras = []
    
    for i in range(5):  # Check first 5 camera indices
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            # Get camera properties
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = int(cap.get(cv2.CAP_PROP_FPS))
            
            available_cameras.append({
                'index': i,
                'width': width,
                'height': height,
                'fps': fps
            })
            cap.release()
    
    if available_cameras:
        print(f"✅ Found {len(available_cameras)} camera(s):")
        for cam in available_cameras:
            print(f"   📹 Camera {cam['index']}: {cam['width']}x{cam['height']} @ {cam['fps']}fps")
    else:
        print("❌ No cameras detected!")
        print("   - Check physical connections")
        print("   - Verify camera permissions")
        print("   - Try running as administrator")
    
    return available_cameras

if __name__ == "__main__":
    print("=" * 50)
    print("🤖 MOHAMED SAIF'S AI CAMERA SYSTEM")
    print("   Inspired by Tony Stark's Technology!")
    print("=" * 50)
    
    # Check available cameras first
    cameras = check_available_cameras()
    
    if cameras:
        print("\n" + "=" * 50)
        # Test camera access
        success = test_camera_access()
        
        if success:
            print("\n🎉 Camera system test completed successfully!")
            print("💡 Your AI can now access the camera just like FRIDAY!")
        else:
            print("\n❌ Camera system test failed!")
            print("🔧 Please check the error messages above for troubleshooting.")
    else:
        print("\n❌ Cannot proceed without camera access!")
    
    print("\n" + "=" * 50)
    print("🚀 Ready to integrate with Ruhi AI Assistant!")
    print("=" * 50)

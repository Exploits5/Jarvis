"""
Jarvis Android Control Module
For Termux - Control Android device functions
"""

import subprocess
import json
import os
from livekit.agents import llm

def run_adb_command(command):
    """Execute ADB command in Termux"""
    try:
        result = subprocess.run(
            f"adb shell {command}",
            shell=True,
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Open App Tool
open = llm.Tool(
    name="open_app",
    description="Open any Android app installed on the device. Example: 'open WhatsApp'",
    arguments={
        "type": "object",
        "properties": {
            "app_name": {
                "type": "string",
                "description": "Name of the app to open (e.g., 'WhatsApp', 'Chrome', 'Instagram')"
            }
        },
        "required": ["app_name"]
    },
)

def open_app_handler(app_name: str) -> str:
    """Open an Android app by name"""
    app_packages = {
        "whatsapp": "com.whatsapp",
        "chrome": "com.android.chrome",
        "instagram": "com.instagram.android",
        "facebook": "com.facebook.katana",
        "twitter": "com.twitter.android",
        "youtube": "com.google.android.youtube",
        "gmail": "com.google.android.gm",
        "telegram": "org.telegram.messenger",
        "settings": "com.android.settings",
        "calculator": "com.android.calculator2",
        "camera": "com.android.camera2",
        "gallery": "com.google.android.gallery",
        "maps": "com.google.android.apps.maps",
        "music": "com.google.android.music",
        "discord": "com.discord",
        "snapchat": "com.snapchat.android",
        "tiktok": "com.zhiliaoapp.musically",
        "reddit": "com.reddit.frontpage",
        "linkedin": "com.linkedin.android",
        "messages": "com.android.messaging",
        "phone": "com.android.phone",
        "contacts": "com.android.contacts",
    }
    
    app_name_lower = app_name.lower()
    package = app_packages.get(app_name_lower, f"com.{app_name_lower}")
    
    command = f"am start -n {package}/.MainActivity || monkey -p {package} 1"
    result = run_adb_command(command)
    return f"✅ Opened {app_name}"

open.call_handler = open_app_handler

# Close App Tool
close = llm.Tool(
    name="close_app",
    description="Close an Android app",
    arguments={
        "type": "object",
        "properties": {
            "app_name": {
                "type": "string",
                "description": "Name of the app to close"
            }
        },
        "required": ["app_name"]
    },
)

def close_app_handler(app_name: str) -> str:
    """Close an Android app"""
    app_packages = {
        "whatsapp": "com.whatsapp",
        "chrome": "com.android.chrome",
        "instagram": "com.instagram.android",
    }
    
    app_name_lower = app_name.lower()
    package = app_packages.get(app_name_lower, f"com.{app_name_lower}")
    
    command = f"am force-stop {package}"
    result = run_adb_command(command)
    return f"✅ Closed {app_name}"

close.call_handler = close_app_handler

# Open Folder/File Tool
folder_file = llm.Tool(
    name="open_folder_file",
    description="Open a folder or file on Android device using file manager",
    arguments={
        "type": "object",
        "properties": {
            "path": {
                "type": "string",
                "description": "Path to folder or file (e.g., '/sdcard/DCIM', '/sdcard/Documents')"
            }
        },
        "required": ["path"]
    },
)

def open_folder_handler(path: str) -> str:
    """Open folder or file in file manager"""
    command = f"am start -a android.intent.action.VIEW -d file://{path} -t \"*/*\""
    result = run_adb_command(command)
    return f"✅ Opened folder/file: {path}"

folder_file.call_handler = open_folder_handler

print("✅ Jarvis Android Control Module Loaded Successfully!")

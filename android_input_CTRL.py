"""
Android Input Control Module for Termux
Handle touch, keyboard, and other input methods
"""

import subprocess
import os
from livekit.agents import llm

def run_adb_command(command):
    """Execute ADB command"""
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

# Move Cursor Tool
move_cursor_tool = llm.Tool(
    name="move_cursor",
    description="Move touch cursor to specific coordinates on Android screen",
    arguments={
        "type": "object",
        "properties": {
            "x": {"type": "integer", "description": "X coordinate"},
            "y": {"type": "integer", "description": "Y coordinate"}
        },
        "required": ["x", "y"]
    },
)

def move_cursor_handler(x: int, y: int) -> str:
    """Move cursor to coordinates"""
    return f"Cursor moved to ({x}, {y})"

move_cursor_tool.call_handler = move_cursor_handler

# Tap Tool (Touch)
tap_tool = llm.Tool(
    name="tap_screen",
    description="Tap/Touch the screen at specific coordinates",
    arguments={
        "type": "object",
        "properties": {
            "x": {"type": "integer", "description": "X coordinate"},
            "y": {"type": "integer", "description": "Y coordinate"}
        },
        "required": ["x", "y"]
    },
)

def tap_handler(x: int, y: int) -> str:
    """Tap screen at coordinates"""
    command = f"input tap {x} {y}"
    result = run_adb_command(command)
    return f"Tapped screen at ({x}, {y})"

tap_tool.call_handler = tap_handler

# Scroll Tool
scroll_tool = llm.Tool(
    name="scroll_screen",
    description="Scroll the screen up or down",
    arguments={
        "type": "object",
        "properties": {
            "x1": {"type": "integer", "description": "Starting X coordinate"},
            "y1": {"type": "integer", "description": "Starting Y coordinate"},
            "x2": {"type": "integer", "description": "Ending X coordinate"},
            "y2": {"type": "integer", "description": "Ending Y coordinate"}
        },
        "required": ["x1", "y1", "x2", "y2"]
    },
)

def scroll_handler(x1: int, y1: int, x2: int, y2: int) -> str:
    """Scroll screen"""
    command = f"input swipe {x1} {y1} {x2} {y2} 500"
    result = run_adb_command(command)
    return f"Scrolled from ({x1}, {y1}) to ({x2}, {y2})"

scroll_tool.call_handler = scroll_handler

# Type Text Tool
type_text_tool = llm.Tool(
    name="type_text",
    description="Type text on the screen",
    arguments={
        "type": "object",
        "properties": {
            "text": {"type": "string", "description": "Text to type"}
        },
        "required": ["text"]
    },
)

def type_text_handler(text: str) -> str:
    """Type text"""
    # Replace spaces with %s for adb command
    formatted_text = text.replace(" ", "%s")
    command = f"input text {formatted_text}"
    result = run_adb_command(command)
    return f"Typed: {text}"

type_text_tool.call_handler = type_text_handler

# Press Key Tool
press_key_tool = llm.Tool(
    name="press_key",
    description="Press a key on the device (e.g., 'BACK', 'HOME', 'ENTER')",
    arguments={
        "type": "object",
        "properties": {
            "key": {"type": "string", "description": "Key to press (BACK, HOME, ENTER, VOLUME_UP, VOLUME_DOWN)"}
        },
        "required": ["key"]
    },
)

def press_key_handler(key: str) -> str:
    """Press a key"""
    key_map = {
        "BACK": "4",
        "HOME": "3",
        "ENTER": "66",
        "VOLUME_UP": "24",
        "VOLUME_DOWN": "25",
        "POWER": "26",
        "MENU": "82"
    }
    
    key_code = key_map.get(key.upper(), key)
    command = f"input keyevent {key_code}"
    result = run_adb_command(command)
    return f"Pressed key: {key}"

press_key_tool.call_handler = press_key_handler

# Swipe Gesture Tool
swipe_gesture_tool = llm.Tool(
    name="swipe_gesture",
    description="Perform a swipe gesture on the screen",
    arguments={
        "type": "object",
        "properties": {
            "direction": {
                "type": "string",
                "description": "Direction to swipe (LEFT, RIGHT, UP, DOWN)"
            }
        },
        "required": ["direction"]
    },
)

def swipe_handler(direction: str) -> str:
    """Perform swipe gesture"""
    # Assuming 1080x1920 screen
    swipes = {
        "LEFT": "800 1000 200 1000 500",
        "RIGHT": "200 1000 800 1000 500",
        "UP": "500 1800 500 200 500",
        "DOWN": "500 200 500 1800 500"
    }
    
    swipe_coords = swipes.get(direction.upper(), swipes["LEFT"])
    command = f"input swipe {swipe_coords}"
    result = run_adb_command(command)
    return f"Swiped {direction}"

swipe_gesture_tool.call_handler = swipe_handler

# Control Volume Tool
control_volume_tool = llm.Tool(
    name="control_volume",
    description="Control device volume",
    arguments={
        "type": "object",
        "properties": {
            "action": {
                "type": "string",
                "description": "Action to perform (UP, DOWN, MUTE, UNMUTE)"
            }
        },
        "required": ["action"]
    },
)

def control_volume_handler(action: str) -> str:
    """Control volume"""
    action_map = {
        "UP": "24",
        "DOWN": "25",
        "MUTE": "91",
        "UNMUTE": "90"
    }
    
    key_code = action_map.get(action.upper(), "25")
    command = f"input keyevent {key_code}"
    result = run_adb_command(command)
    return f"Volume action: {action}"

control_volume_tool.call_handler = control_volume_handler

print("✅ Android Input Control Module Loaded Successfully!")

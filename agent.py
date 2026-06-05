from dotenv import load_dotenv
import sys
import os

# Detect if running on Android/Termux
IS_ANDROID = 'TERMUX_VERSION' in os.environ or (sys.platform.startswith('linux') and 'arm' in os.uname().machine)

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import (
    google,
    noise_cancellation,
)
from Jarvis_prompts import behavior_prompts, Reply_prompts
from Jarvis_google_search import google_search, get_current_datetime
from jarvis_get_whether import get_weather

# Import Android-specific modules if on Termux
if IS_ANDROID:
    try:
        from Jarvis_android_CTRL import open, close, folder_file
        from android_input_CTRL import move_cursor_tool, tap_tool, scroll_tool, type_text_tool, press_key_tool, swipe_gesture_tool, control_volume_tool
    except ImportError:
        print("⚠️  Android modules not found. Falling back to standard imports.")
        from Jarvis_window_CTRL import open, close, folder_file
        from keyboard_mouse_CTRL import move_cursor_tool, mouse_click_tool, scroll_cursor_tool, type_text_tool, press_key_tool, swipe_gesture_tool, press_hotkey_tool, control_volume_tool
else:
    from Jarvis_window_CTRL import open, close, folder_file
    from keyboard_mouse_CTRL import move_cursor_tool, mouse_click_tool, scroll_cursor_tool, type_text_tool, press_key_tool, swipe_gesture_tool, press_hotkey_tool, control_volume_tool

from Jarvis_file_opner import Play_file

load_dotenv()

platform_name = 'Android/Termux' if IS_ANDROID else 'Windows/Linux'
print(f"🤖 Jarvis Starting... Platform: {platform_name}")

class Assistant(Agent):
    def __init__(self) -> None:
        if IS_ANDROID:
            try:
                tools = [
                    google_search,
                    get_current_datetime,
                    get_weather,
                    open,           # ऐप्स खोलें
                    close,          # ऐप्स बंद करें
                    folder_file,    # फोल्डर खोलें
                    Play_file,      # फाइल चलाएं
                    move_cursor_tool,      # कर्सर move करें
                    tap_tool,              # टैप/टच करें
                    scroll_tool,           # स्क्रॉल करें
                    type_text_tool,        # टेक्स्ट लिखें
                    press_key_tool,        # की दबाएं
                    swipe_gesture_tool,    # स्वाइप करें
                    control_volume_tool    # वॉल्यूम कंट्रोल करें
                ]
            except:
                tools = [
                    google_search,
                    get_current_datetime,
                    get_weather,
                    open, close, folder_file, Play_file,
                    move_cursor_tool, mouse_click_tool, scroll_cursor_tool,
                    type_text_tool, press_key_tool, swipe_gesture_tool,
                    press_hotkey_tool, control_volume_tool
                ]
        else:
            tools = [
                google_search,
                get_current_datetime,
                get_weather,
                open,           # ऐप्स खोलें
                close,          # ऐप्स बंद करें
                folder_file,    # फोल्डर खोलें
                Play_file,      # फाइल चलाएं
                move_cursor_tool,      # कर्सर move करें
                mouse_click_tool,      # माउस क्लिक करें
                scroll_cursor_tool,    # स्क्रॉल करें
                type_text_tool,        # टेक्स्ट लिखें
                press_key_tool,        # की दबाएं
                press_hotkey_tool,     # hotkey दबाएं
                swipe_gesture_tool,    # स्वाइप करें
                control_volume_tool    # वॉल्यूम कंट्रोल करें
            ]
        
        super().__init__(instructions=behavior_prompts, tools=tools)


async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        llm=google.beta.realtime.RealtimeModel(
            voice="Charon"
        )
    )
    
    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC(),
            video_enabled=True 
        ),
    )

    await ctx.connect()

    await session.generate_reply(
        instructions=Reply_prompts
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))

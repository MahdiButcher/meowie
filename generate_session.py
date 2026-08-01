import os
import asyncio
from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.sessions import StringSession

load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")


async def generate_session():
    print("--- Telethon StringSession Generator ---")
    
    api_id = API_ID or input("Enter your API_ID: ").strip()
    api_hash = API_HASH or input("Enter your API_HASH: ").strip()
    
    if not api_id or not api_hash:
        print("API_ID and API_HASH are required.")
        return

    # Interactive session creation directly in local terminal
    async with TelegramClient(StringSession(), int(api_id), api_hash) as client:
        session_str = client.session.save()
        print("\n" + "=" * 50)
        print("Your StringSession (Keep this secret!):")
        print("=" * 50)
        print(session_str)
        print("=" * 50 + "\n")
        
        # Send a test confirmation message to Saved Messages
        try:
            await client.send_message("me", "✅ Session initialized successfully!")
            print("Confirmation message sent to your Telegram Saved Messages.")
        except Exception as e:
            print(f"Notice: Could not send test message to Saved Messages: {e}")


if __name__ == "__main__":
    asyncio.run(generate_session())

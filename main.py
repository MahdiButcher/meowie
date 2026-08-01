import os
import logging
from dotenv import load_dotenv
from telethon import TelegramClient, events

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not API_ID or not API_HASH or not BOT_TOKEN:
    logger.warning(
        "Please provide API_ID, API_HASH, and BOT_TOKEN in .env file before running!"
    )

# Initialize the Telethon Bot Client
client = TelegramClient("meowie_bot_session", int(API_ID) if API_ID else 0, API_HASH if API_HASH else "")


@client.on(events.NewMessage(pattern=r"^/start$"))
async def start_handler(event):
    """Handler for /start command."""
    user = await event.get_sender()
    first_name = user.first_name if user and user.first_name else "there"
    await event.respond(f"Hello, {first_name}! 🐾 Meowie bot is up and running!")


@client.on(events.NewMessage(pattern=r"^/ping$"))
async def ping_handler(event):
    """Handler for /ping command."""
    await event.respond("Pong! 🐱")


@client.on(events.NewMessage)
async def echo_handler(event):
    """Echo non-command messages."""
    if event.text and not event.text.startswith("/"):
        await event.respond(f"Meowie says: {event.text}")


def main():
    if not API_ID or not API_HASH or not BOT_TOKEN:
        print("Error: Missing credentials. Please set API_ID, API_HASH, and BOT_TOKEN in .env")
        return

    print("Starting Meowie Telethon Bot...")
    client.start(bot_token=BOT_TOKEN)
    client.run_until_disconnected()


if __name__ == "__main__":
    main()

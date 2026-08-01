import os
import sqlite3
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

# Directory for persistent data (sessions & database)
DATA_DIR = os.getenv("DATA_DIR", "data")
os.makedirs(DATA_DIR, exist_ok=True)

# Database file path
DB_PATH = os.path.join(DATA_DIR, "meowie.db")
# Telethon session file path
SESSION_PATH = os.path.join(DATA_DIR, "meowie_bot_session")


def init_db():
    """Initialize SQLite database for user interaction logging."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            first_name TEXT,
            last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.commit()
    conn.close()
    logger.info(f"Database initialized at {DB_PATH}")


def save_user(user):
    """Save or update user details in the SQLite database."""
    if not user:
        return
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO users (user_id, username, first_name, last_seen)
        VALUES (?, ?, ?, CURRENT_TIMESTAMP)
        ON CONFLICT(user_id) DO UPDATE SET
            username=excluded.username,
            first_name=excluded.first_name,
            last_seen=CURRENT_TIMESTAMP
        """,
        (user.id, user.username, user.first_name),
    )
    conn.commit()
    conn.close()


# Initialize Telethon Client with persistent session path
client = TelegramClient(
    SESSION_PATH,
    int(API_ID) if API_ID else 0,
    API_HASH if API_HASH else "",
)


@client.on(events.NewMessage(pattern=r"^/start$"))
async def start_handler(event):
    """Handler for /start command."""
    user = await event.get_sender()
    save_user(user)
    first_name = user.first_name if user and user.first_name else "there"
    await event.respond(f"Hello, {first_name}! 🐾 Meowie bot is up and running!")


@client.on(events.NewMessage(pattern=r"^/ping$"))
async def ping_handler(event):
    """Handler for /ping command."""
    user = await event.get_sender()
    save_user(user)
    await event.respond("Pong! 🐱")


@client.on(events.NewMessage)
async def echo_handler(event):
    """Echo non-command messages."""
    if event.text and not event.text.startswith("/"):
        user = await event.get_sender()
        save_user(user)
        await event.respond(f"Meowie says: {event.text}")


def main():
    if not API_ID or not API_HASH or not BOT_TOKEN:
        logger.error("Missing credentials. Please set API_ID, API_HASH, and BOT_TOKEN in .env")
        print("Error: Missing credentials. Please set API_ID, API_HASH, and BOT_TOKEN in .env")
        return

    init_db()
    print(f"Starting Meowie Telethon Bot with session at {SESSION_PATH}...")
    client.start(bot_token=BOT_TOKEN)
    client.run_until_disconnected()


if __name__ == "__main__":
    main()

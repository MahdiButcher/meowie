# Meowie 🐾

A simple Telegram Bot project built using [Telethon](https://github.com/LonamiWebs/Telethon) in Python with Docker support, persistent storage for sessions/SQLite database, and a local interactive CLI session generator script.

## Features
- `/start` - Greets user & logs user details into SQLite database.
- `/ping` - Responds with `Pong! 🐱`
- Echoes incoming non-command text messages.
- Docker & Docker Compose setup with persistent volume for Telethon session and database files.
- `generate_session.py` - Local terminal CLI helper to safely authenticate user client sessions.

## Prerequisites
- Python 3.8+ (or Docker & Docker Compose)
- Telegram API credentials (`API_ID`, `API_HASH` from [my.telegram.org](https://my.telegram.org))
- Telegram Bot Token from [@BotFather](https://t.me/BotFather)

## Configuration

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Fill in `API_ID`, `API_HASH`, and `BOT_TOKEN` in `.env`.

---

## Safe Local Session Generator

To generate a Telethon `StringSession` for userbot automation safely in your local terminal:

```bash
python generate_session.py
```
*(Interactive prompts will safely accept phone numbers, OTPs, and 2FA passwords directly inside your local console without exposing credentials to any third-party bot or server).*

---

## Running with Docker Compose (Recommended)

Start the bot in detached mode with persistent volume storage (`meowie_data` mounted at `/app/data`):

```bash
docker-compose up -d --build
```

View logs:
```bash
docker-compose logs -f
```

Stop the bot:
```bash
docker-compose down
```

---

## Running Locally

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the bot:**
   ```bash
   python main.py
   ```

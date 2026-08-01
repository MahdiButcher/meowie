# Meowie 🐾

A simple Telegram Bot project built using [Telethon](https://github.com/LonamiWebs/Telethon) in Python.

## Features
- `/start` - Greets the user.
- `/ping` - Responds with `Pong! 🐱`
- Echoes incoming non-command text messages.

## Prerequisites
- Python 3.8+
- Telegram API credentials (`API_ID`, `API_HASH` from [my.telegram.org](https://my.telegram.org))
- Telegram Bot Token from [@BotFather](https://t.me/BotFather)

## Setup & Running

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MahdiButcher/meowie.git
   cd meowie
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**
   Copy `.env.example` to `.env` and fill in your Telegram API details:
   ```bash
   cp .env.example .env
   ```

4. **Run the bot:**
   ```bash
   python main.py
   ```

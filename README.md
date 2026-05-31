# Discord First Bot

A simple Discord bot built with `discord.py`, featuring slash commands:

- `/ping` — check the bot is responding
- `/info` — show server name and member count
- `/help` — list available commands

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Copy `.env.example` to `.env` and add your bot token:
   ```bash
   cp .env.example .env
   # then edit .env and set DISCORD_TOKEN=...
   ```
   Get a token from the [Discord Developer Portal](https://discord.com/developers/applications).
3. Run the bot:
   ```bash
   python first-bot.py
   ```

> The token is loaded from the `DISCORD_TOKEN` environment variable and is never committed.

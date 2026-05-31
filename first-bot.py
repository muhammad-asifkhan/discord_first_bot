import os

import discord
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    await tree.sync()
    print(f'Logged in as {client.user}')


# /ping
@tree.command(name="ping", description="Check bot response")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")


# /info
@tree.command(name="info", description="Show server info")
async def info(interaction: discord.Interaction):

    guild = interaction.guild

    server_name = guild.name
    member_count = guild.member_count

    msg = f"""
Server Name: {server_name}
Members: {member_count}
"""

    await interaction.response.send_message(msg)


# /help
@tree.command(name="help", description="Show all commands")
async def help_command(interaction: discord.Interaction):

    msg = """
Available Commands:

/ping  -> Check bot status
/info  -> Show server info
/help  -> Show all commands
"""

    await interaction.response.send_message(msg)


# Token is read from the DISCORD_TOKEN environment variable (.env file, gitignored).
token = os.getenv("DISCORD_TOKEN")
if not token:
    raise SystemExit("Set DISCORD_TOKEN in a .env file (see .env.example).")
client.run(token)
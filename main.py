import discord
from discord.ext import commands
import json
from discord import Webhook, AsyncWebhookAdapter
import git
import re

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


with open("config.json") as meow:
    prefix = json.load(meow)["prefix"]

bot_intents = discord.Intents.default()
bot_intents.members = True

client = commands.Bot(command_prefix=prefix, intents=bot_intents, fetch_offline_members=True, case_insensitive=True)


@client.event
async def on_ready():
    print(f'{bcolors.OKGREEN}Logged on as {client.user}!{bcolors.ENDC}')


@client.listen('on_message')
async def on_message(message):
    print(f'{bcolors.OKCYAN}Message from {message.author}: {message.content}{bcolors.ENDC}')
    with open("config.json") as meow:
        fmales = json.load(meow["bad-f*males"])
        if message.author.id in fmales:
            if re.finditer(r"\b(fumo)(s\b|\b)", message.content, re.IGNORECASE):
                await message.delete()


with open("config.json") as meow:
    token = json.load(meow)["token"]

# client = MyClient()
client.run(token)

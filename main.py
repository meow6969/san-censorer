import discord
from discord.ext import commands
import json
from discord import Webhook, AsyncWebhookAdapter
import git
import re
import aiohttp


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


# bot_intents = discord.Intents.default()
# bot_intents.members = True

client = commands.Bot(command_prefix='meow', case_insensitive=True)


@client.event
async def on_ready():
    print(f'{bcolors.OKGREEN}Logged on as {client.user}!{bcolors.ENDC}')


@client.listen('on_message')
async def on_message(message):
    print(f'{bcolors.OKCYAN}Message from {message.author}: {message.content}{bcolors.ENDC}')
    with open("config.json") as meow:
        fmales = json.load(meow)["bad-f*males"]
        if message.author.id in fmales:
            if re.finditer(r"\b(fumo)(s\b|\b)", message.content, re.IGNORECASE):
                await message.delete()
                # async with aiohttp.ClientSession() as session:
                #     webhook = Webhook.from_url(i.url, adapter=AsyncWebhookAdapter(session))
                success = False
                for i in await message.channel.webhooks():
                    if i.channel == message.channel:
                        if i.name == '_fumo':
                            async with aiohttp.ClientSession() as session:
                                webhook = Webhook.from_url(i.url, adapter=AsyncWebhookAdapter(session))
                                success = True
                                if message.author.nick is None:
                                    nick = message.author
                                await webhook.send("@everyone i love fumos!!!!",
                                                   username=str(nick),
                                                   avatar_url=message.author.avatar_url)
                if not success:
                    await message.channel.create_webhook(name="_fumo")
                    for i in await message.guild.webhooks():
                        if i.channel == message.channel:
                            if i.name == '_fumo':
                                async with aiohttp.ClientSession() as session:
                                    webhook = Webhook.from_url(i.url, adapter=AsyncWebhookAdapter(session))
                                    if message.author.nick is None:
                                        nick = message.author
                                    await webhook.send("@everyone i love fumos!!!!",
                                                       username=str(nick),
                                                       avatar_url=message.author.avatar_url)


with open("config.json") as meow:
    token = json.load(meow)["token"]

# client = MyClient()
client.run(token)

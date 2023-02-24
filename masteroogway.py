import importlib
import discord
import logging

# import the Tensorflow algorithm into the main script
algorithm = input('algorithm')
importlib.import_module(algorithm)

# add discord intents and instantiate the discord client
intents = discord.Intents.default()
intents = True
client = discord.Client(intents = intents)


handler = logging.FileHandler(filename="masteroogwayerr.log", encoding="utf-8", mode="w")

# chatbot events
@client.event
async def on_ready(self):
    print("Logged in, I am.")

@client.event
async def on_message(self, message):
    if message.author == client.user:
        return

    if message.content.startsWith("?"):
        # get stuff from the tensorflow algorithm
        print("you know what")




# runs the bot
client.run("token here", log_handler = handler, log_level = logging.DEBUG)

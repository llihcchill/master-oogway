import discord
import logging
from algorithm import run_algorithm

# add discord intents and instantiate the discord client
intents = discord.Intents.default()
intents = True
client = discord.Client(intents = intents)

# if errors occur, this function will print them out into a file called "masteroogwayerr.log"
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
        # initialise question and array to store the quote
        question = message.content
        quote = []
        run_algorithm(question, quote)

        # send a message for the quote in italic (make it look good as well)

# runs the bot
client.run("token here", log_handler = handler, log_level = logging.DEBUG)

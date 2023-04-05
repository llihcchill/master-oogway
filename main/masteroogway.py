import discord
import logging
from understand import understand_question

# add discord intents and instantiate the discord client
intents = discord.Intents.default()
client = discord.Client(intents = intents)
quote = []
# if errors occur, this function will print them out into a file called "masteroogwayerr.log"
handler = logging.FileHandler(filename="masteroogwayerr.log", encoding="utf-8", mode="w")

# chatbot events
@client.event
async def on_ready(self):
    print("Logged in, I am.")

@client.event
async def on_message(self, message):
    # tests to see if the message sent is from itself
    if message.author == client.user:
        return
    else:
        print(f"Logged in as {self.user}")

    if message.content.startsWith("?"):
        # initialise question and array to store the quote
        question = message.content

        # run run_algorithm function to find perfect quote
        understand_question.get_quote(question, quote)

# turns the reply into an embed
@client.command()
async def embed(ctx):
    # make an embed of the quote so it looks good
    embed = discord.Embed(colour="2a9ead", title=f"Dear {ctx.author.display_name}", description=f"*{str(quote[0])}*")
    embed.set_footer(text="*- Master Oogway*")

    # sends the embedded quote to the channel
    await ctx.send(embed=embed)

# runs the bot
client.run("token here", log_handler = handler, log_level = logging.DEBUG)

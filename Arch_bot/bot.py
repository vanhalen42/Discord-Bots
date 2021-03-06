# import the discord library

import discord
from discord import message
from discord import embeds
import os
import random
from dotenv import load_dotenv
load_dotenv()

# bot connect
client = discord.Client()
# this variable stores id of an output channel, you can have many variables corresponding to different channels
out_channel = int(os.getenv("OUT_CHANNEL"))  # add default out_channel

motor_functions = [0]


@client.event
# new event
async def on_ready():
    # output_channel object holds the info of that channel, whos id is provided
    output_channel = client.get_channel(out_channel)
    # code to send message is
    await output_channel.send("I use Arch btw.")
# add links or messages according to your convinience
spam_list = []
anime_list=[]

@client.event
async def on_message(message):
    output_channel = message.channel
    if message.content == "ok bro you only" and message.author.id == int(os.getenv("ADMIN")):
        motor_functions[0] = 1
    if message.content == "arch supremacy" and message.author.id == int(os.getenv("ADMIN")):
        motor_functions[0] = 0
    input_mssg = message.content  # message.content is the string of that message
    if "arch" in input_mssg.lower():
        if motor_functions[0] == 0 and message.author.id != client.user.id:
            await output_channel.send(random.choice(spam_list))

# Run the client on this server
client.run(os.getenv('BOT_TOKEN'))  # add a bot token

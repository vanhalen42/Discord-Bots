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
out_channel = int(os.getenv("OUT_CHANNEL")) # add default out_channel

motor_functions = [0]


@client.event
# new event
async def on_ready():
    # output_channel object holds the info of that channel, whos id is provided
    output_channel = client.get_channel(out_channel)
    # code to send message is
    # await output_channel.send("I art been summoneth.")


@client.event
async def on_message(message):
    output_channel = message.channel
    if message.content == "too much F now" and message.author.id == int(os.getenv("ADMIN")):
        motor_functions[0] = 1
    if message.content == "continue rr" and message.author.id == int(os.getenv("ADMIN")):
        motor_functions[0] = 0
    input_mssg = message.content  # message.content is the string of that message
    if input_mssg[0] == 'F' and motor_functions[0] == 0:
        mssg = input_mssg.split(" ", 1)
        command = mssg[0]
        if command=='F' or command == 'f':
            str = mssg[1]*5 + "\n" + mssg[1] + "\n" + mssg[1] + "\n" + mssg[1]*4 + \
                "\n" + mssg[1] + "\n" + mssg[1] + \
                "\n" + mssg[1] + "\n" + mssg[1]
            # print(str)
            var=random.randint(0, 9)
            if var == 5 or var ==7:
                await output_channel.send(str)
            else:
                await output_channel.send("Go do osn noobde.")

# Run the client on this server
client.run(os.getenv('BOT_TOKEN')) # add a bot token

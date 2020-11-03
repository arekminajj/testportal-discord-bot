import discord
from discord.ext import commands
from validator_collection import validators, checkers
import os
import testportal
import glob
import shutil

client = commands.Bot(command_prefix='.')

def deleteScreenshots():
    folder = 'screenshots'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

@client.command()
async def test(ctx, *, url):
    if(checkers.is_url(url)):
        await ctx.send("Just a sec...")
        await testportal.getTest(url)
        screenshots = os.listdir('screenshots')
        lenght = len(screenshots)
        for x in range(lenght):
            await ctx.send(file=discord.File('screenshots\screenshot' + str(x+1) + '.png'))
        deleteScreenshots()
    else:
        await ctx.send("The Url is not valid")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

client.run('')
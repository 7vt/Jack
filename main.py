





#ACCOUNT FILE MUST BE LOWERCASED
print("Made by Uzi")
import discord,json,os,random
from discord.ext import commands

with open("config.json") as file: # load config
    info = json.load(file)
    token = info["token"]
    delete = info["autodelete"]
    prefix = info["prefix"]

bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print("Jack Runnin!")
@bot.command() # Stock Check Command 
async def stock(ctx):
    stockmenu = discord.Embed(title="Account Stock",description="") # def embed
    for filename in os.listdir("Accounts"):
        with open("Accounts\\"+filename) as f: # every file on accounts folder
            ammount = len(f.read().splitlines()) # amount of lines
            name = (filename[0].upper() + filename[1:].lower()).replace(".txt","") 
            stockmenu.description += f"*{name}* - {ammount}\n" # embed add
    await ctx.send(embed=stockmenu) # embed sent



@bot.command() # the main command (gen)
async def gen(ctx,name=None):
    if name == None:
        await ctx.send("Specify what type of account you want!") 
    else:
        name = name.lower()+".txt" # .txt ext add
        if name not in os.listdir("Accounts"): # if name not in directory
            await ctx.send(f"Account does not exist  `{prefix}stock`")
        else:
            with open("Accounts\\"+name) as file:
                lines = file.read().splitlines() # read lines
            if len(lines) == 0: # if empty file
                await ctx.send("Sorry! Theres no stock!") 
            else:
                with open("Accounts\\"+name) as file:
                    account = random.choice(lines) # Get a random account
                try: # try to dm
                    await ctx.author.send(f"`{str(account)}`\n\This message will delete in {str(delete)} seconds!",delete_after=delete)
                except: # if fail
                    await ctx.send("Error, please enable your DMs.")
                else: # file removes 300 seconds
                    await ctx.send("Sent account, check your DMs!")
                    with open("Accounts\\"+name,"w") as file:
                        file.write("") # clear file
                    with open("Accounts\\"+name,"a") as file:
                        for line in lines: # add lines back
                            if line != account: # no added
                                file.write(line+"\n")

@bot.command()
async def credits(ctx):
    await ctx.send('Made by Uzi')


bot.run(token)

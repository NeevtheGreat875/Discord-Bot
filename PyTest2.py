import discord
from discord.ext import commands
import random
client = commands.Bot(command_prefix = "@")

@client.event
async def on_ready():
    print("Bot Is Ready")
    
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)} ms")

@client.command(aliases = ["8ball", "fortuneTeller"])
async def _8ball(ctx, *, question):
    responses = ["I am not sure", "Certainly Dude", "Do you see that nuclear sign, ask me again I'll drop it on you >:)", "Absolutely Not", "Yeah Sure!"]
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

@client.command()
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit = amount)
    
@client.command()
async def kick(ctx, member : discord.Member, *, reason = "Not Specified Reasons"):
    await member.kick(reason=reason)
    await ctx.send(f"{member} was kicked {reason}")
    
@client.command()
async def rps(ctx, playerChoice):
    pythonChoice = random.choice(["Rock", "Paper", "Scissors"])
    
    await ctx.send(f"You Chose: {playerChoice} And I Chose: {pythonChoice}")
    
    if pythonChoice == playerChoice:
        await ctx.send("Tie!!")
    elif pythonChoice == "Scissors" and playerChoice == "Paper":
        await ctx.send("Ha! I win you Lose")
    elif pythonChoice == "Rock" and playerChoice == "Scissors":
        await ctx.send("Ha! I win you Lose")
    elif pythonChoice == "Paper" and playerChoice == "Rock":
        await ctx.send("Ha! I win you Lose")
    elif pythonChoice == "Paper" and playerChoice == "Scissors":
        await ctx.send("NO! You win I LOSE")
    elif pythonChoice == "Rock" and playerChoice == "Paper":
        await ctx.send("NO! You win I LOSE")
    elif pythonChoice == "Scissors" and playerChoice == "Rock":
        await ctx.send("NO! You win I LOSE")
    else:
        await ctx.send("You tried to cheat! CHEATER!! >(")

@client.command()
async def spam(ctx, word, noOfTime = 100):
    num = 0
    if noOfTime <= 300:
        while num <= noOfTime and noOfTime:
            await ctx.send(word)
            num = num + 1
    else:
        await ctx.send("You idiot I am spammy but not that much! >:")
        
client.run('')

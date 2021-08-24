import chatbot
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
	print("Bot is ready.")

@bot.command()
async def hello(ctx):
	await ctx.send("hi")

@bot.event
async def on_message(message):
	if message.channel.name == "alienbot-channel" or message.channel.name == "admin":
		if message.author.id == bot.user.id: # hey bot, don't talk to yourself
			return
		botMessage = chatbot.get_response(message.content.lower())
		await message.channel.send(botMessage)

bot.run('put discord api key here')

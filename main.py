import discord
from discord.ext import commands

intents = discord.Intents(guilds=True, reactions=True, members=True)
Bot = commands.Bot(command_prefix='!', intents=intents)

token = open('token.txt','r').read()


@Bot.event
async def on_ready():
    print('Ready for action! 💥')


badwords = ['bad', 'words', 'here']


@Bot.event
async def on_message(message):
    for i in badwords:  # Go through the list of bad words;
        if i in message.content:
            await message.delete()
            await message.channel.send(f"{message.author.mention} Don't use that word!")
            Bot.dispatch('profanity', message, i)
            return  # So that it doesn't try to delete the message again, which will cause an error.
    await Bot.process_commands(message)


@Bot.event
async def on_profanity(message, word):
    channel = Bot.get_channel(888431396350214177)  # for me it's bot.get_channel(817421787289485322)
    embed = discord.Embed(title="Logger!", description=f"{message.author.name} : {word}",
                          color=discord.Color.blurple())  # Let's make an embed!
    await channel.send(embed=embed)


@Bot.event
async def on_member_join(member):
    channel = Bot.get_channel(888431396350214177)
    await channel.send(f'{member} Aramıza hoş geldin.')

@Bot.event
async def on_member_remove(member):
    channel = Bot.get_channel(888431396350214177)
    await channel.send(f'{member} Aramızdan ayrıldı.')


@Bot.command()
async def deneme(msg):
    await msg.send(f'Deneme123 {msg.author.name}!')


@Bot.command()
async def hello(msg):
    await msg.send(f"Hello {msg.author.name}!")  # f-string


#@Bot.command(name='invite', description='Create an invite link')

Bot.run(token)

import discord
import random

TOKEN = 'your bot token here'

client = discord.Client()

# fortunes cookie quotes the bot will reply with when messaged for !advice
fortunes = ['Stop wishing. Start doing.' ,
            'if love someone a lot tell it before its too late',
            'For success today look first to yourself.',
            'An unexpected aquaintance will resurface.' ,
            'You are given the chance to take part in an exciting adventure.' ,
            'Soon, a visitor shall delight you.' ,
            'You are very talented in many ways.' ,
            'The eyes believe themselves; the ears believe other people.' ,
            'Your difficult work will get payoff today.' ,
            'All the water in the world cant sink a ship unless it gets inside.',
            'Good news from afar may bring you a welcome visitor.',
            'May you someday be carbon neutral.',
            'Your tongue is your ambassador',
            'Life is too short to waste time hating anyone.',
            'He who throws dirt is losing ground.',
            'Make a wise choice everyday.',
            'Failure is not defeat until you stop trying.',
            'Keep true to the dreams of your youth. ',
            'Soon you will be sitting on top of the world.',
            'Be calm when confronting an emergency crisis.',
            'Land is always on the mind of a flying bird.',
            'Trust your intuition.']

# bot login message
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# recording the chat messages, needed for responses and advice
@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

# chat messages for the bot to respond too, ignoring the bot itself
    if message.author == client.user:
        return
    if message.channel.name == 'your discord channel here':
        # hello responses
        if user_message.lower() == 'hey bud':
            await message.channel.send(f'Hey {username}!')
            return
        # goodbye responses
        elif user_message.lower() == 'bye':
            await message.channel.send(f'Later {username}!')
            return
        # give fortune cookie advice
        elif user_message.lower() == '!advice':
            await message.channel.send(random.choice(fortunes))
            return

client.run(TOKEN)

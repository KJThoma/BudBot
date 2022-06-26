import discord
import random
import requests
import json

TOKEN = 'your token here'

client = discord.Client()

# function for advice API
def get_advice():
    response = requests.get('https://api.adviceslip.com/advice')
    json_data = json.loads(response.text)
    quote = json_data['slip']
    return(quote['advice'])

# coin flip results
coin_flip = ['heads', 'tails']

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    if message.channel.name == 'your channel here':
        # hello responses
        if user_message.lower() == 'hey bud':
            await message.channel.send(f'Hey {username}!'))
            return
        # goodbye responses
        elif user_message.lower() == 'bye':
            await message.channel.send(f'Later {username}!')
            return
        # give fortune cookie advice
        elif user_message.lower() == '!advice':
            advice = get_advice()
            await message.channel.send(advice)
            return
        # random number generator
        elif user_message.lower() == '!roll':
            random_number = random.randint(1, 100)
            await message.channel.send(random_number)
            return
        # coin flip
        elif user_message.lower() == '!coinflip':
            await message.channel.send(random.choice(coin_flip))
            return

client.run(TOKEN)

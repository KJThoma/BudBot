import discord
import random
import re
import requests
import json
import giphy_client
from giphy_client.rest import ApiException

# tokens to use APIs
discord_token = 'discord bot token here'
giphy_token = 'giphy token here'

# for discord intents requirements (see pycord doc)
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# giphy API variable
api_instance = giphy_client.DefaultApi()

# function for advice API
def get_advice():
    response = requests.get('https://api.adviceslip.com/advice')
    json_data = json.loads(response.text)
    quote = json_data['slip']
    return(quote['advice'])

# function for giphy search
def search_gifs(query):
    try:
        response = api_instance.gifs_search_get(giphy_token, query, limit=5, rating='r')
        # Extracting URLs from the response
        gif_urls = [gif.url for gif in response.data]
        # Choosing a random GIF URL
        random_gif_url = random.choice(gif_urls) if gif_urls else None
        return random_gif_url
    except ApiException as e:
        return f"Exception when calling DefaultApi->gifs_search_get: {e}"

# hey messages
hey_lines = ['Hey Bud!',
       'Hi Friend!',
       'Hello There!']

# coin flip results
coin_flip = ['heads', 'tails']

# confirm budbot is ready
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# events to action on in specified channel
@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    if message.channel.name == 'channel name here':
        # hello responses
        if user_message.lower() == 'hey':
            await message.channel.send(random.choice(hey_lines))
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
        # search for a gif
        elif user_message.lower().startswith('!gif '):
            query = user_message[len('!gif '):]
            gif_url = search_gifs(query)

            if gif_url:
                # Sending just the random GIF URL
                await message.channel.send(gif_url)
            else:
                await message.channel.send('No GIF found')
            return
        # fxtwitter links
        elif re.match(r'https?://(www\.)?twitter\.com/[^ ]+', user_message.lower()):
            fx_twitter = re.sub(r'https?://(www\.)?twitter\.com', r'https://fxtwitter.com', user_message)
            message_text = 'Use this FixTweet URL: ' + fx_twitter
            await message.channel.send(message_text)
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

client.run(discord_token)

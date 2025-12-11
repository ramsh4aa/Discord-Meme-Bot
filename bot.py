import requests
import json

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']


import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # Prevent replying to itself
        if message.author == self.user:
            return
        
        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())

# Set up intents (permissions)
intents = discord.Intents.default()
intents.message_content = True

# Create the bot client
client = MyClient(intents=intents)

# Start the bot (replace YOUR_TOKEN_HERE)
client.run('your_token_here')

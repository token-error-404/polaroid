import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('MTMwMDg1NDk3MDQ3OTkzNTQ4OQ.GikiET.DPqBPN35FNvov3NxaDxJItpyRu6MB48DDU7eog')

import discord
import os
from dotenv import load_dotenv
import random
from keep_alive import keep_alive

sad = ['sad', 'Sad', 'Suicide', 'upset', 'pain', 'suicide']
randoms = ['Yes', 'No', 'Why', 'Okay', 'Sure', 'Here', 'Now', 'Later']


client = discord.Client()
prefix = ';'
my_secret = os.environ['TOKEN']
rick = os.environ['Rick']


@client.event
async def on_ready():
  # CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
	for guild in client.guilds:
		# PRINT THE SERVER'S ID AND NAME.
		print(f"- {guild.id} (name: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
		guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	print("SSBot is in " + str(guild_count) + " guilds.")
  

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    msgsend = message.channel.send
 
    if msg.startswith(prefix + 'hello'):
        await msgsend('Hello!')

    if msg.startswith(prefix + 'rick'):
        await msgsend(rick)

    if msg.startswith(prefix + 'buymeaxbox'):
        await msgsend('no')

    if msg.startswith(prefix + 'random'):
        await msgsend(random.choice(randoms))

    if msg.startswith(prefix + 'yes'):
        await msgsend('no')

    if msg.startswith(prefix + 'no'):
        await msgsend('yes')

    if msg.startswith(prefix + 'help'):
        await msgsend(
            ";Hello: says hello \n;rick: can\'t tell you. \n;buymeaxbox: no \n;random: Pick from a random list of words \n;yes: no \n;no: yes \n;A10: You can guess \n;E: E"
        )

    if msg.startswith(prefix + 'A10'):
      await msgsend('brrrrrrrrrrrrrrrrrrrrrt')

    if msg.startswith(prefix + 'E'):
      await msgsend('EA Sports')

    if msg.startswith(prefix + 'info'):
      await msgsend('Developed by Alex Doss & Sam Honkanen')
    
    if msg.startswith(prefix + '9Adm1n'):
      await msgsend('This is an admin tool, bot is working correctly.')

    if any(word in msg for word in sad):
      await msgsend("It'll be alright, you're time is short.")

  
    

keep_alive()
client.run(my_secret)

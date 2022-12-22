import discord, random, re, os
from retar import aliv


intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print('mrow mrow this is spri')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('hi'):
    await message.channel.send('MROW??')

  if 'spri' in message.content.lower():
    tx = ['mrow mrow', 'prrrprprrrr', ':3', 'hissssss']
    await message.channel.send(random.choice(tx))

  if 'pspsps' in message.content.lower():
    await message.channel.send(
      'https://tenor.com/view/sprigatito-cat-pokemon-gif-25462173')

  if 'good girl' in message.content.lower():
    await message.channel.send(':3')

  if '=menu' in message.content.lower():
    await message.channel.send(
      'https://cdn.discordapp.com/attachments/1030706592380887040/1035162221807939634/unknown.png'
    )

  if 'weed' in message.content.lower():
    await message.channel.send(
      'https://tenor.com/view/sprigatito-pokemon-weed-cat-gif-25019907')


  match = re.findall("rock|paper|scissors",
                     message.content,
                     flags=re.IGNORECASE)

  if match:
    player = match[0]
    options = ['rock', 'paper', 'scissors']
    sprich = random.choice(options)
    w = [
      "you won. mew die die die die meowowo",
      "take this W bc it's the only one u have", "take this W and kys"
    ]
    l = [
      "ur a sore ass loser", "hah loser kys",
      "i win LMAO imagine losing to a weedcat"
    ]
    await message.reply(f"i choose {sprich}!!!")
    if player == sprich:
      await message.channel.send("it's tied up!! like ur mom was last night :3")
    elif player == "rock" and sprich == "scissors":
      await message.channel.send(random.choice(w))
    elif player == "paper" and sprich == "rock":
      await message.channel.send(random.choice(w))
    elif player == "scissors" and sprich == "paper":
      await message.channel.send(random.choice(w))
    elif player == "rock" and sprich == "paper":
      await message.channel.send(random.choice(l))
    elif player == "paper" and sprich == "scissors":
      await message.channel.send(random.choice(l))
    else:
      await message.channel.send(random.choice(l))

  if message.content.startswith('!spr dice'):
    num = ['1', '2', '3', '4', '5', '6']
    await message.channel.send(f"you rolled a {random.choice(num)}")
    await message.channel.send(
      'https://tenor.com/view/sprigatito-spinning-cat-grass-green-gif-25204424'
    )

  if '!spr 1 or 2' in message.content.lower():
    n = ['1', '2']
    await message.channel.send(f"i think you should do {random.choice(n)}")
    await message.channel.send(
      'https://tenor.com/view/pokemon-pokemon-scarlet-and-violet-pokemon-scarlet-pokemon-violet-sprigatito-gif-25833283'
    )

aliv()
client.run(os.environ['token'])

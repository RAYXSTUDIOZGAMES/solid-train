import discord, os

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.dnd,
        activity=discord.Game("Under Maintenance")
    )
    print("Bot online")

client.run(os.getenv("DISCORD_TOKEN"))

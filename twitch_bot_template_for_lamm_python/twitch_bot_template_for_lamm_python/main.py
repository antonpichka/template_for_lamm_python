from twitchio.ext import commands

## Remove two "QQ" on the left and right    
token = "QQ_4p7y8d2fhql49ubqbb23pb3xd9lcjm_QQ"
channel = "dejeanco"

bot = commands.Bot(
    token=token, 
    prefix="!",
    initial_channels=[channel]
)

@bot.command()
async def hello(ctx: commands.Context):
    await ctx.send("World")

bot.run()
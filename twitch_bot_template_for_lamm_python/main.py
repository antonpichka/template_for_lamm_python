from twitchio.ext import commands

## Client ID: x33lfux0xqz6gzt9jkgaagupnl6zqy
## Client Secret: 2boyqf9am3e5n8zadm12341cakeic6
## 5/30/2024 - https://id.twitch.tv/oauth2/token
## {"access_token":"f54va1kndqiywpgtyfo0u1cgqua9dh","expires_in":5207674,"token_type":"bearer"}
## Remove two "QQ" on the left and right    
token = "f54va1kndqiywpgtyfo0u1cgqua9dh"
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
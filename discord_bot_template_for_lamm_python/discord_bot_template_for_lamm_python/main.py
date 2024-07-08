import asyncio
import functools
import discord
from discord.ext import commands
from discord_bot_template_for_lamm_python.named_vm.kirill_vm.kirill_vm import KirillVM
from discord_bot_template_for_lamm_python.named_vm.test_vm.test_vm import TestVM
from library_architecture_mvvm_modify_python import BaseModelRepository, EnumRWTMode
from discord_bot_template_for_lamm_python.named_utility.keys_api_utility import KeysAPIUtility

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

BaseModelRepository.enum_rwt_mode = EnumRWTMode.TEST
token = "MTI0NDE2ODE1NDY1ODI0MjU4MA.GdghOZ.xHk5k7Hf5wMLBGE5b3Kch_0fvOuDlABiWLUYwQ"
name_bot = "test_bot#3697"
first_message_w_sending_channel = "Commands:\n- /test @member\n- /kirill"
sending_channel_id = 1244204490153005068
receiving_channel_id = 1244204698529959997  

@bot.event
async def on_message(message: discord.Message):
    if message.author == bot.user:
        return
    if message.channel.id != sending_channel_id:
        return
    sending_channel = bot.get_channel(sending_channel_id)
    member_role = discord.utils.get(sending_channel.guild.roles, name="member")
    await sending_channel.set_permissions(member_role, send_messages=False)
    await asyncio.sleep(2)
    list_message = []
    necessary_item_history = None
    async for item_history in sending_channel.history(limit=None):
        if str(item_history.author) == name_bot and item_history.content == first_message_w_sending_channel:
            necessary_item_history = item_history
            continue
        list_message.append(item_history)
    for item_message in list_message:
        await item_message.delete() 
    if necessary_item_history is None:
        await sending_channel.send(first_message_w_sending_channel) 
        await bot.process_commands(message)
        await sending_channel.set_permissions(member_role, send_messages=True)
        return
    await bot.process_commands(message)
    await sending_channel.set_permissions(member_role, send_messages=True)

@bot.command()
async def test(context: commands.Context, member: discord.Member) -> None:
    test_w_init_w_build_w_callback_w_exception = functools.partial(__test_w_init_w_build_w_callback_w_exception, context, member)
    test_w_init_w_build_w_callback_w_success = functools.partial(__test_w_init_w_build_w_callback_w_success, context, member)
    test_vm = TestVM(member.id)
    await test_vm.init_w_build(test_w_init_w_build_w_callback_w_exception,test_w_init_w_build_w_callback_w_success)
    test_vm.dispose()

@bot.command()
async def kirill(context: commands.Context) -> None:
    kirill_w_init_w_build_w_callback_w_exception = functools.partial(__kirill_w_init_w_build_w_callback_w_exception, context)
    kirill_w_init_w_build_w_callback_w_success = functools.partial(__kirill_w_init_w_build_w_callback_w_success, context)
    kirill_vm = KirillVM()
    await kirill_vm.init_w_build(kirill_w_init_w_build_w_callback_w_exception,kirill_w_init_w_build_w_callback_w_success)
    kirill_vm.dispose()

async def __test_w_init_w_build_w_callback_w_exception(_: commands.Context, member: discord.Member, msg: str) -> None:
    channel = bot.get_channel(receiving_channel_id)
    await channel.send(msg)

async def __test_w_init_w_build_w_callback_w_success(_: commands.Context, member: discord.Member, msg: str) -> None:
    channel = bot.get_channel(receiving_channel_id)
    await channel.send("Hello, " + member.mention + "!. Your current rating: " + msg + " ELO")

async def __kirill_w_init_w_build_w_callback_w_exception(_: commands.Context, msg: str) -> None:
    channel = bot.get_channel(receiving_channel_id)
    await channel.send(msg)

async def __kirill_w_init_w_build_w_callback_w_success(_: commands.Context, msg: str) -> None:
    channel = bot.get_channel(receiving_channel_id)
    await channel.send(msg)

## Add a bot: https://discord.com/oauth2/authorize?client_id=1244168154658242580&permissions=8&scope=bot
bot.run(token)
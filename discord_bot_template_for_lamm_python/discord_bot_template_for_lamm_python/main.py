import asyncio
import functools
import discord
from discord.ext import commands
from discord_bot_template_for_lamm_python.env import *
from discord_bot_template_for_lamm_python.named_vm.kirill_vm.kirill_vm import KirillVM
from discord_bot_template_for_lamm_python.named_vm.test_vm.test_vm import TestVM
from library_architecture_mvvm_modify_python import BaseModelRepository, EnumRWTMode

if RELEASE_W_TEST == "RELEASE":
    BaseModelRepository.enum_rwt_mode = EnumRWTMode.RELEASE
else:
    BaseModelRepository.enum_rwt_mode = EnumRWTMode.TEST

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)  

@bot.event
async def on_message(message: discord.Message):
    if message.author == bot.user:
        return
    if message.channel.id != SENDING_CHANNEL_ID:
        return
    sending_channel = bot.get_channel(SENDING_CHANNEL_ID)
    member_role = discord.utils.get(sending_channel.guild.roles, name="member")
    await sending_channel.set_permissions(member_role, send_messages=False)
    await asyncio.sleep(2)
    list_message = []
    necessary_item_history = None
    async for item_history in sending_channel.history(limit=None):
        if str(item_history.author) == NAME_BOT and item_history.content == FIRST_MESSAGE_W_SENDING_CHANNEL:
            necessary_item_history = item_history
            continue
        list_message.append(item_history)
    for item_message in list_message:
        await item_message.delete() 
    if necessary_item_history is None:
        await sending_channel.send(FIRST_MESSAGE_W_SENDING_CHANNEL) 
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
    channel = bot.get_channel(RECEIVING_CHANNEL_ID)
    await channel.send(msg)

async def __test_w_init_w_build_w_callback_w_success(_: commands.Context, member: discord.Member, msg: str) -> None:
    channel = bot.get_channel(RECEIVING_CHANNEL_ID)
    await channel.send("Hello, " + member.mention + "!. Your current rating: " + msg + " ELO")

async def __kirill_w_init_w_build_w_callback_w_exception(_: commands.Context, msg: str) -> None:
    channel = bot.get_channel(RECEIVING_CHANNEL_ID)
    await channel.send(msg)

async def __kirill_w_init_w_build_w_callback_w_success(_: commands.Context, msg: str) -> None:
    channel = bot.get_channel(RECEIVING_CHANNEL_ID)
    await channel.send(msg)

## Add a bot: https://discord.com/oauth2/authorize?client_id=1244168154658242580&permissions=8&scope=bot
bot.run(API_BOT_TOKEN)
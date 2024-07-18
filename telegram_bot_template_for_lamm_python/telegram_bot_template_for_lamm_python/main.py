import functools
from telethon import TelegramClient, events
from telegram_bot_template_for_lamm_python.env import *
from telegram_bot_template_for_lamm_python.named_vm.test_vm.test_vm import TestVM
from library_architecture_mvvm_modify_python import BaseModelRepository, EnumRWTMode

if RELEASE_W_TEST == "RELEASE":
    BaseModelRepository.enum_rwt_mode = EnumRWTMode.RELEASE
else:
    BaseModelRepository.enum_rwt_mode = EnumRWTMode.TEST
    
client = TelegramClient("bot", API_ID, API_HASH).start(bot_token=API_BOT_TOKEN)

@client.on(events.NewMessage(pattern="/test"))
async def test(event):
    test_w_init_w_build_w_callback_w_exception = functools.partial(__test_w_init_w_build_w_callback_w_exception, event)
    test_w_init_w_build_w_callback_w_success = functools.partial(__test_w_init_w_build_w_callback_w_success, event)
    test_vm = TestVM()
    await test_vm.init_w_build(test_w_init_w_build_w_callback_w_exception,test_w_init_w_build_w_callback_w_success)
    test_vm.dispose()

@client.on(events.NewMessage(pattern=r"/text\s+(.*)"))
async def text(event):
    text = event.pattern_match.group(1)
    await event.respond(text)

@client.on(events.NewMessage(pattern="/info"))
async def info(event):
    str_users = ""
    async for item_user in client.iter_participants(event.chat_id): 
        if item_user.deleted:
            continue
        str_users += "id: " + str(item_user.id) + ", username: " + item_user.username + "\n"
    await event.respond(str_users)

async def __test_w_init_w_build_w_callback_w_success(event, msg: str) -> None:
    await event.respond("You called classes TestVM: " + msg)

async def __test_w_init_w_build_w_callback_w_exception(event, msg: str) -> None:
    await event.respond(msg)

client.run_until_disconnected()
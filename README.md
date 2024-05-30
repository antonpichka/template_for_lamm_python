- https://github.com/antonpichka/library_architecture_mvvm_modify/tree/main/package#architectural-objects
- https://github.com/antonpichka/template_for_lamm_python/tree/main/discord_bot_template_for_lamm_python/discord_bot_template_for_lamm_python/named_vm/example_vm
- https://github.com/antonpichka/library_architecture_mvvm_modify/labels

---

- After setup. Everything after this message can be deleted. Even the message itself

## Project setup

- [discord_bot_template_for_lamm_python](https://github.com/antonpichka/template_for_lamm_python#discord_bot_template_for_lamm_python)

### discord_bot_template_for_lamm_python

-  If you need to change the application name from 'discord_bot_template_for_lamm_python' to 'discord_bot_${your_name}':
- - 'discord_bot_template_for_lamm_python/discord_bot_template_for_lamm_python'
- - - 'discord_bot_template_for_lamm_python' to 'discord_bot_${your_name}':
- - 'discord_bot_template_for_lamm_python/setup.py'
- - - 'name=discord_bot_template_for_lamm_python'
- - - 'packages=[...]'
- - - Change your project's dependency path in "discord_bot_template_for_lamm_python"
```  
entry_points={
        "console_scripts": [
            "program = discord_bot_template_for_lamm_python.main:main",
            "q = discord_bot_template_for_lamm_python.named_test_main.q:main"
        ]
    }
```

## Note

- The Telegram bot works in the same way as the Discord bot. Here is an example of running the 'main.py' telegram bot using the 'pyTelegramBotAPI' library:
```
import telebot

bot = telebot.TeleBot("YOUR_BOT_TOKEN")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

bot.infinity_polling()
```

- I don’t recommend developing a twitch bot, and here’s why (Used the 'twitchio' library):
- - To launch a Twitch bot with the bot name, you need to use curl to make a request to receive a token, where you must specify 2 parameters 'client_id', 'client_secret'. After receiving the token, we enter the source code as in Discord Bot and Telegram Bot, but we need to write down which Twitch channels to send the bot to, which already creates a problem, because why enter channels if you can do it like in Discord (to connect Discord Bot we need URL link to this bot, and you’re done) or Telegram (we enter the username of the bot in the search, and use it, and you’re done). In general, you need to create a mini-site in order to add Twtich Bot to your channel through Twitch integration, or maybe there is another way, but this already creates a lot of inconvenience compared to Discord Bot and Telegram Bot. But even after all this it will write the error AttributeError: 'NoneType' object has no attribute 'cancel'
Unclosed client session
client_session: <aiohttp.client.ClientSession object at 0x000001C9715E8BF0>
Unclosed connector
connections: ['[(<aiohttp.client_proto.ResponseHandler object at 0x000001C971BF0C50>, 681114.64)]']
connector: <aiohttp.connector.TCPConnector object at 0x000001C971842510>.
- - To launch a Twitch bot on behalf of a channel, you need to go to the website (https://twitchtokengenerator.com/) and go through the twitch integration to get a token, and then use it. But this bot can only be used on a specific channel and on behalf of the channel administrator, which no longer allows sharing the bot on other channels
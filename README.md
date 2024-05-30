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
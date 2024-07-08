from setuptools import setup

setup(
    name="discord_bot_template_for_lamm_python",
    version="0.0.1",
    packages=[
        "discord_bot_template_for_lamm_python",
        "discord_bot_template_for_lamm_python.model_repository.example_repository",
        "discord_bot_template_for_lamm_python.model_repository.rating_repository",
        "discord_bot_template_for_lamm_python.model_repository.task_repository",
        "discord_bot_template_for_lamm_python.model_repository.user_repository",
        "discord_bot_template_for_lamm_python.model.example",
        "discord_bot_template_for_lamm_python.model.rating",
        "discord_bot_template_for_lamm_python.model.task",
        "discord_bot_template_for_lamm_python.model.user",
        "discord_bot_template_for_lamm_python.named_test_main",
        "discord_bot_template_for_lamm_python.named_utility",
        "discord_bot_template_for_lamm_python.named_vm.kirill_vm",
        "discord_bot_template_for_lamm_python.named_vm.test_vm"
    ],
    install_requires=[
        "library-architecture-mvvm-modify-python==3.0.1",
        "discord.py==2.3.2"
    ],
    entry_points={
        "console_scripts": [
            "start = discord_bot_template_for_lamm_python.main:main",
            "q_test_main = discord_bot_template_for_lamm_python.named_test_main.q_test_main:main",
            "keys_api_utility_test_main = discord_bot_template_for_lamm_python.named_test_main.keys_api_utility_test_main:main"
        ]
    }
)
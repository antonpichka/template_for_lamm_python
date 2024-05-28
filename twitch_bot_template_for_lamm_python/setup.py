from setuptools import setup

setup(
    name="twitch_bot_template_for_lamm_python",
    version="0.0.1",
    packages=[
        "twitch_bot_template_for_lamm_python",
        "twitch_bot_template_for_lamm_python.model.rating",
        "twitch_bot_template_for_lamm_python.model.task",
        "twitch_bot_template_for_lamm_python.model.user",
        "twitch_bot_template_for_lamm_python.named_test_main",
        "twitch_bot_template_for_lamm_python.named_utility",
        "twitch_bot_template_for_lamm_python.named_vm.kirill_vm",
        "twitch_bot_template_for_lamm_python.named_vm.test_vm"
    ],
    install_requires=[
        "library-architecture-mvvm-modify-python==1.0.0",
        "twitchio==2.9.1"
    ],
    entry_points={
        "console_scripts": [
            "program = twitch_bot_template_for_lamm_python.main:main",
            "q = twitch_bot_template_for_lamm_python.named_test_main.q:main"
        ]
    }
)
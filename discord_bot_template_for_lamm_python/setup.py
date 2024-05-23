from setuptools import setup

setup(
    name="discord_bot_template_for_lamm_python",
    version="0.0.1",
    install_requires=[
        "library-architecture-mvvm-modify-python",
        "discord.py==2.3.2"
    ],
    entry_points={
        "console_scripts": [
            "program = main:main"
        ]
    }
)
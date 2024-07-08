from setuptools import setup

setup(
    name="telegram_bot_template_for_lamm_python",
    version="0.0.1",
    packages=[
        "telegram_bot_template_for_lamm_python",
        "telegram_bot_template_for_lamm_python.named_test_main",
        "telegram_bot_template_for_lamm_python.named_utility"
    ],
    install_requires=[
        "library-architecture-mvvm-modify-python==3.0.1",
        "pyTelegramBotAPI==4.18.1"
    ],
    entry_points={
        "console_scripts": [
            "start = telegram_bot_template_for_lamm_python.main:main",
            "q_test_main = telegram_bot_template_for_lamm_python.named_test_main.q_test_main:main"
        ]
    }
)
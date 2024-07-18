from setuptools import setup

setup(
    name="telegram_bot_template_for_lamm_python",
    version="0.0.1",
    packages=[
        "telegram_bot_template_for_lamm_python",
        "telegram_bot_template_for_lamm_python.model_repository.example_repository",
        "telegram_bot_template_for_lamm_python.model_repository.rating_repository",
        "telegram_bot_template_for_lamm_python.model_repository.task_repository",
        "telegram_bot_template_for_lamm_python.model_repository.user_repository",
        "telegram_bot_template_for_lamm_python.model.example",
        "telegram_bot_template_for_lamm_python.model.rating",
        "telegram_bot_template_for_lamm_python.model.task",
        "telegram_bot_template_for_lamm_python.model.user",
        "telegram_bot_template_for_lamm_python.named_test_main",
        "telegram_bot_template_for_lamm_python.named_utility",
        "telegram_bot_template_for_lamm_python.named_vm.example_vm",
        "telegram_bot_template_for_lamm_python.named_vm.kirill_vm",
        "telegram_bot_template_for_lamm_python.named_vm.test_vm"
    ],
    install_requires=[
        "library-architecture-mvvm-modify-python==3.0.2",
        "Telethon==1.36.0"
    ],
    entry_points={
        "console_scripts": [
            "program = telegram_bot_template_for_lamm_python.main:main",
            "q_test_main = telegram_bot_template_for_lamm_python.named_test_main.q_test_main:main"
        ]
    }
)
from typing import final
from telegram_bot_template_for_lamm_python.model_repository.example_repository.example_repository import ExampleRepository

@final
class FactoryObjectUtility():
    def __init__(self):
        pass

    def __init__(self):
        pass

    # ModelRepository #
    @staticmethod
    def get_example_repository() -> 'ExampleRepository':
        return ExampleRepository()
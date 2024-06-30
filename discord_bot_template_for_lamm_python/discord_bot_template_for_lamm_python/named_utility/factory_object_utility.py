from typing import final
from discord_bot_template_for_lamm_python.model_repository.rating_repository.rating_repository import RatingRepository
from discord_bot_template_for_lamm_python.model_repository.task_repository.task_repository import TaskRepository
from discord_bot_template_for_lamm_python.model_repository.user_repository.user_repository import UserRepository
from discord_bot_template_for_lamm_python.model_repository.example_repository.example_repository import ExampleRepository

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
    
    @staticmethod
    def get_rating_repository() -> 'RatingRepository':
        return RatingRepository()
    
    @staticmethod
    def get_task_repository() -> 'TaskRepository':
        return TaskRepository()
    
    @staticmethod
    def get_user_repository() -> 'UserRepository':
        return UserRepository()
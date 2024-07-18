from typing import final
from library_architecture_mvvm_modify_python import *
from telegram_bot_template_for_lamm_python.model_repository.rating_repository.rating_repository import RatingRepository
from telegram_bot_template_for_lamm_python.model_repository.task_repository.task_repository import TaskRepository
from telegram_bot_template_for_lamm_python.model_repository.user_repository.user_repository import UserRepository
from telegram_bot_template_for_lamm_python.model_repository.example_repository.example_repository import ExampleRepository
from telegram_bot_template_for_lamm_python.named_vm.kirill_vm.data_for_kirill_vm import DataForKirillVM
from telegram_bot_template_for_lamm_python.model.task.list_task import ListTask
from telegram_bot_template_for_lamm_python.model.task.task import Task
from telegram_bot_template_for_lamm_python.named_vm.test_vm.data_for_test_vm import DataForTestVM
from telegram_bot_template_for_lamm_python.model.rating.rating import Rating
from telegram_bot_template_for_lamm_python.named_vm.example_vm.data_for_example_vm import DataForExampleVM

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
    
    # NamedState #
    @staticmethod
    def get_named_state_where_data_w_example_vm() -> 'BaseNamedState':
        return DefaultState[DataForExampleVM](DataForExampleVM(False))
    
    @staticmethod
    def get_named_state_where_data_w_kirill_vm() -> 'BaseNamedState':
        return DefaultState[DataForKirillVM](DataForKirillVM(False,ListTask[Task]([])))
    
    @staticmethod
    def get_named_state_where_data_w_test_vm() -> 'BaseNamedState':
        return DefaultState[DataForTestVM](DataForTestVM(False))
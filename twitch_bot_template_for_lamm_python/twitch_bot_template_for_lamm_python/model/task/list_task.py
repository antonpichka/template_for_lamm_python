from typing import TypeVar
from library_architecture_mvvm_modify_python import *
from discord_bot_template_for_lamm_python.model.task.task import Task

T = TypeVar("T", bound=Task)

class ListTask(Generic[T],BaseListModel[T]):
    def __init__(self, list_model: list[T]) -> None:
        super().__init__(list_model)
    
    def get_clone(self) -> 'ListTask':
        new_list_model: list[T] = []
        for item_model in self.LIST_MODEL:
            new_list_model.append(item_model.get_clone())
        return ListTask(new_list_model)
    
    def to_string(self) -> str:
        str_list_model = "\n"
        for item_model in self.LIST_MODEL:
            str_list_model += item_model.to_string() + ",\n"
        return "ListTasks(listModel: [" + str_list_model + "])"
    
    def get_str_where_name_by_task_parameter_list_model(self) -> str:
        str_list_model = "Tasks for Kirill: \n"
        for item_model in self.LIST_MODEL:
            str_list_model += "- - " + item_model.NAME + "\n"
        return str_list_model
from typing import TypeVar
from library_architecture_mvvm_modify_python import *
from telegram_bot_template_for_lamm_python.model.user.user import User

T = TypeVar("T", bound=User)

class ListUser(Generic[T],BaseListModel[T]):
    def __init__(self, list_model: list[T]) -> None:
        super().__init__(list_model)
    
    def get_clone(self) -> 'ListUser':
        new_list_model: list[T] = []
        for item_model in self.LIST_MODEL:
            new_list_model.append(item_model.get_clone())
        return ListUser(new_list_model)
    
    def to_string(self) -> str:
        str_list_model = "\n"
        for item_model in self.LIST_MODEL:
            str_list_model += item_model.to_string() + ",\n"
        return "ListUser(listModel: [" + str_list_model + "])"
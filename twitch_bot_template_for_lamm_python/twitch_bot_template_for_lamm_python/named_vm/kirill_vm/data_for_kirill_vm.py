from typing import final
from library_architecture_mvvm_modify_python import *
from discord_bot_template_for_lamm_python.model.task.list_task import ListTask
from discord_bot_template_for_lamm_python.model.task.task import Task
from discord_bot_template_for_lamm_python.named_vm.kirill_vm.enum_data_for_kirill_vm import EnumDataForKirillVM

@final
class DataForKirillVM(BaseDataForNamed[EnumDataForKirillVM]):
    def __init__(self, is_loading: bool, list_task: ListTask[Task]) -> None:
        super().__init__(is_loading)
        self.list_task: ListTask[Task] = list_task
    
    def get_enum_data_for_named(self) -> EnumDataForKirillVM:
        if self.exception_controller.is_where_not_equals_null_parameter_exception():
            return EnumDataForKirillVM.EXCEPTION
        return EnumDataForKirillVM.SUCCESS 
    
    def to_string(self) -> str:
        return "DataForKirillVM(is_loading: " + str(self.is_loading)  + ", exception_controller: " + self.exception_controller.to_string() + ", list_task: " + self.list_task.to_string() + ")"
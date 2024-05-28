from typing import final
from library_architecture_mvvm_modify_python import *
from discord_bot_template_for_lamm_python.named_vm.example_vm.enum_data_for_example_vm import EnumDataForExampleVM

@final
class DataForExampleVM(BaseDataForNamed[EnumDataForExampleVM]):
    def __init__(self, is_loading: bool) -> None:
        super().__init__(is_loading)
    
    def get_enum_data_for_named(self) -> EnumDataForExampleVM:
        if self.exception_controller.is_where_not_equals_null_parameter_exception():
            return EnumDataForExampleVM.EXCEPTION
        return EnumDataForExampleVM.SUCCESS 
    
    def to_string(self) -> str:
        return "DataForExampleVM(is_loading: " + str(self.is_loading) + ", exception_controller: " + self.exception_controller.to_string() + ")"
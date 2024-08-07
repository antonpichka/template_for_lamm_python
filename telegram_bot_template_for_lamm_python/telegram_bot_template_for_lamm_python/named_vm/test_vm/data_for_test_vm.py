from typing import final
from library_architecture_mvvm_modify_python import *
from telegram_bot_template_for_lamm_python.named_vm.test_vm.enum_data_for_test_vm import EnumDataForTestVM

@final
class DataForTestVM(BaseDataForNamed[EnumDataForTestVM]):
    def __init__(self, is_loading: bool) -> None:
        super().__init__(is_loading)
    
    def get_enum_data_for_named(self) -> EnumDataForTestVM:
        if self.exception_controller.is_where_not_equals_null_parameter_exception():
            return EnumDataForTestVM.EXCEPTION
        return EnumDataForTestVM.SUCCESS 
    
    def to_string(self) -> str:
        return "DataForTestVM(is_loading: " + str(self.is_loading) + ", exception_controller: " + self.exception_controller.to_string() + ")" 
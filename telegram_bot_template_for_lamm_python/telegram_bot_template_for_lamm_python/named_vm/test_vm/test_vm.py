from typing import Callable, final
from library_architecture_mvvm_modify_python import *
from telegram_bot_template_for_lamm_python.named_utility.ready_data_utility import ReadyDataUtility
from telegram_bot_template_for_lamm_python.named_vm.test_vm.data_for_test_vm import DataForTestVM
from telegram_bot_template_for_lamm_python.named_vm.test_vm.enum_data_for_test_vm import EnumDataForTestVM
from telegram_bot_template_for_lamm_python.named_utility.factory_object_utility import FactoryObjectUtility

@final
class TestVM():
    def __init__(self) -> None:
        ## ModelRepository
        ## NamedUtility

        ## NamedState
        self.__NAMED_STATE: BaseNamedState[DataForTestVM] = FactoryObjectUtility.get_named_state_where_data_w_test_vm()
    
    async def init_w_build(self, callback_w_exception: Callable[[str], None], callback_w_success: Callable[[str], None]) -> None:
        first_request = await self.__first_request()
        debug_print("TestVM: " + first_request)
        data_for_named = self.__NAMED_STATE.get_data_for_named()
        match data_for_named.get_enum_data_for_named():
            case EnumDataForTestVM.EXCEPTION:
                return await callback_w_exception(data_for_named.exception_controller.get_key_parameter_exception())
            case EnumDataForTestVM.SUCCESS:
                return await callback_w_success("SUCCESS")

    def dispose(self) -> None:
        self.__NAMED_STATE.dispose()
         
    async def __first_request(self) -> str:
        return ReadyDataUtility.SUCCESS
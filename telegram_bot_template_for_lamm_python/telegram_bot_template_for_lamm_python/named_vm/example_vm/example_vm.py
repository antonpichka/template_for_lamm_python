import asyncio
from typing import Callable, final
from library_architecture_mvvm_modify_python import *
from telegram_bot_template_for_lamm_python.named_vm.example_vm.data_for_example_vm import DataForExampleVM
from telegram_bot_template_for_lamm_python.named_vm.example_vm.enum_data_for_example_vm import EnumDataForExampleVM
from telegram_bot_template_for_lamm_python.named_utility.ready_data_utility import ReadyDataUtility

@final
class ExampleVM():
    def __init__(self) -> None:
        ## ModelRepository
        ## NamedUtility

        ## NamedState
        self.__NAMED_STATE: BaseNamedState[DataForExampleVM] = DefaultState[DataForExampleVM](DataForExampleVM(False))
    
    async def init_w_build(self, callback_w_exception: Callable[[str], None], callback_w_success: Callable[[str], None]) -> None:
        first_request = await self.__first_request()
        debug_print("ExampleVM: " + first_request)
        data_for_named = self.__NAMED_STATE.get_data_for_named()
        match data_for_named.get_enum_data_for_named():
            case EnumDataForExampleVM.EXCEPTION:
                return await callback_w_exception(data_for_named.exception_controller.get_key_parameter_exception())
            case EnumDataForExampleVM.SUCCESS:
                return await callback_w_success("Success")

    def dispose(self) -> None:
        self.__NAMED_STATE.dispose()

    async def __first_request(self) -> str:
        await asyncio.sleep(1)
        return ReadyDataUtility.SUCCESS
import asyncio
from typing import Callable, final
from library_architecture_mvvm_modify_python import *
from discord_bot_template_for_lamm_python.named_utility.ready_data_utility import ReadyDataUtility
from discord_bot_template_for_lamm_python.named_utility.factory_object_utility import FactoryObjectUtility
from discord_bot_template_for_lamm_python.named_vm.example_vm.data_for_example_vm import DataForExampleVM
from discord_bot_template_for_lamm_python.named_vm.example_vm.enum_data_for_example_vm import EnumDataForExampleVM

@final
class ExampleVM():
    def __init__(self) -> None:
        ## ModelRepository
        ## NamedUtility

        ## NamedState
        self.__NAMED_STATE: BaseNamedState[DataForExampleVM] = FactoryObjectUtility.get_named_state_where_data_w_example_vm()
    
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
import asyncio
from typing import Callable, final
from library_architecture_mvvm_modify_python import *
from discord_bot_template_for_lamm_python.named_utility.keys_success_utility import KeysSuccessUtility
from discord_bot_template_for_lamm_python.named_vm.example_vm.data_for_example_vm import DataForExampleVM
from discord_bot_template_for_lamm_python.named_vm.example_vm.enum_data_for_example_vm import EnumDataForExampleVM

@final
class ExampleVM():
    def __init__(self) -> None:
        ## OperationEEModel(EEWhereNamed)[EEFromNamed]EEParameterNamedService
        ## NamedUtility

        ## Main objects 
        self.__NAMED_STATE: BaseNamedState[DataForExampleVM] = DefaultState[DataForExampleVM](DataForExampleVM(False))
        self.__RWT_MODE: RWTMode = RWTMode(
            EnumRWTMode.TEST,
            [
                NamedCallback("init",self.__init_release_callback)
            ],
            [
                NamedCallback("init",self.__init_test_callback)
            ]
        )
    
    async def init_w_build(self, callback_w_exception: Callable[[str], None], callback_w_success: Callable[[str], None]) -> None:
        callback = await self.__RWT_MODE.get_named_callback_from_name("init").CALLBACK()
        debug_print("ExampleVM: " + callback)
        data_for_named = self.__NAMED_STATE.get_data_for_named()
        match data_for_named.get_enum_data_for_named():
            case EnumDataForExampleVM.EXCEPTION:
                return await callback_w_exception(data_for_named.exception_controller.get_key_parameter_exception())
            case EnumDataForExampleVM.SUCCESS:
                return await callback_w_success("Success")

    def dispose(self) -> None:
        self.__NAMED_STATE.dispose()

    async def __init_release_callback(self) -> str:
        await asyncio.sleep(1)
        return KeysSuccessUtility.SUCCESS
         
    async def __init_test_callback(self) -> str:
        return KeysSuccessUtility.SUCCESS
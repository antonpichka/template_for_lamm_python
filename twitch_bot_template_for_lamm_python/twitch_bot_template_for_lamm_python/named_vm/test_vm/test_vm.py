import asyncio
from typing import Callable, final
from library_architecture_mvvm_modify_python import *
from discord_bot_template_for_lamm_python.model.rating.rating import Rating
from discord_bot_template_for_lamm_python.model.user.user import User
from discord_bot_template_for_lamm_python.named_utility.keys_success_utility import KeysSuccessUtility
from discord_bot_template_for_lamm_python.named_vm.test_vm.data_for_test_vm import DataForTestVM
from discord_bot_template_for_lamm_python.named_vm.test_vm.enum_data_for_test_vm import EnumDataForTestVM

@final
class TestVM():
    def __init__(self, discord_id: int) -> None:
        ## OperationEEModel(EEWhereNamed)[EEFromNamed]EEParameterNamedService
        ## NamedUtility

        ## Main objects 
        self.__NAMED_STATE: BaseNamedState[DataForTestVM] = DefaultState[DataForTestVM](DataForTestVM(False,discord_id,Rating("",0)))
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
        debug_print("TestVM: " + callback)
        data_for_named = self.__NAMED_STATE.get_data_for_named()
        match data_for_named.get_enum_data_for_named():
            case EnumDataForTestVM.EXCEPTION:
                return await callback_w_exception(data_for_named.exception_controller.get_key_parameter_exception())
            case EnumDataForTestVM.SUCCESS:
                return await callback_w_success(data_for_named.rating.get_str_parameter_elo())

    def dispose(self) -> None:
        self.__NAMED_STATE.dispose()

    async def __init_release_callback(self) -> str:
        await asyncio.sleep(1)
        return KeysSuccessUtility.SUCCESS
         
    async def __init_test_callback(self) -> str:
        ## Simulation get "User" from "discord_id"
        user = User("19593a8a-e8ad-42c0-a4ff-aedc42005570", self.__NAMED_STATE.get_data_for_named().discord_id)
        await asyncio.sleep(1)
        ## Simulation get "Rating" from "unique_id_by_user"
        rating = Rating(user.UNIQUE_ID, 322)
        await asyncio.sleep(1)
        self.__NAMED_STATE.get_data_for_named().rating = rating.get_clone()
        return KeysSuccessUtility.SUCCESS
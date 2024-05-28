import asyncio
from typing import Callable, final
from library_architecture_mvvm_modify_python import *
from discord_bot_template_for_lamm_python.model.task.list_task import ListTask
from discord_bot_template_for_lamm_python.model.task.task import Task
from discord_bot_template_for_lamm_python.named_utility.keys_success_utility import KeysSuccessUtility
from discord_bot_template_for_lamm_python.named_vm.kirill_vm.data_for_kirill_vm import DataForKirillVM
from discord_bot_template_for_lamm_python.named_vm.kirill_vm.enum_data_for_kirill_vm import EnumDataForKirillVM

@final
class KirillVM():
    def __init__(self) -> None:
        ## OperationEEModel(EEWhereNamed)[EEFromNamed]EEParameterNamedService
        ## NamedUtility

        ## Main objects
        self.__NAMED_STATE: BaseNamedState[DataForKirillVM] = DefaultState[DataForKirillVM](DataForKirillVM(False,ListTask[Task]([])))
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
        debug_print("KirillVM: " + callback)
        data_for_named = self.__NAMED_STATE.get_data_for_named()
        match data_for_named.get_enum_data_for_named():
            case EnumDataForKirillVM.EXCEPTION:
                return await callback_w_exception(data_for_named.exception_controller.get_key_parameter_exception())
            case EnumDataForKirillVM.SUCCESS:
                return await callback_w_success(data_for_named.list_task.get_str_where_name_by_task_parameter_list_model())
    
    def dispose(self) -> None:
        self.__NAMED_STATE.dispose()

    async def __init_release_callback(self) -> str:
        await asyncio.sleep(1)
        return KeysSuccessUtility.SUCCESS
         
    async def __init_test_callback(self) -> str:
        ## Simulation get "ListTask"
        list_task = ListTask[Task](
            [
                Task("be6096e7-7fc8-423f-b84a-d95c07387b0b","Brush your teeth"),
                Task("785e8d87-df1b-491c-bcb0-0005a374658a","Do a workout"),
                Task("133d5f2f-f3dc-4819-ad49-b84b254e077e","Eat"),
                Task("14b9a2de-082a-4b95-a154-096d9526ddc4","Sleep"),
            ])
        await asyncio.sleep(1)
        self.__NAMED_STATE.get_data_for_named().list_task = list_task.get_clone()
        return KeysSuccessUtility.SUCCESS
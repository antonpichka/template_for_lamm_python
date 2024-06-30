from typing import Callable, final
from library_architecture_mvvm_modify_python import *
from discord_bot_template_for_lamm_python.model_repository.task_repository.task_repository import TaskRepository
from discord_bot_template_for_lamm_python.named_utility.ready_data_utility import ReadyDataUtility
from discord_bot_template_for_lamm_python.model.task.list_task import ListTask
from discord_bot_template_for_lamm_python.model.task.task import Task
from discord_bot_template_for_lamm_python.named_vm.kirill_vm.data_for_kirill_vm import DataForKirillVM
from discord_bot_template_for_lamm_python.named_vm.kirill_vm.enum_data_for_kirill_vm import EnumDataForKirillVM
from discord_bot_template_for_lamm_python.named_utility.factory_object_utility import FactoryObjectUtility

@final
class KirillVM():
    def __init__(self) -> None:
        ## ModelRepository
        self.__TASK_REPOSITORY: TaskRepository = FactoryObjectUtility.get_task_repository()

        ## NamedUtility

        ## NamedState
        self.__NAMED_STATE: BaseNamedState[DataForKirillVM] = DefaultState[DataForKirillVM](DataForKirillVM(False,ListTask[Task]([])))

    async def init_w_build(self, callback_w_exception: Callable[[str], None], callback_w_success: Callable[[str], None]) -> None:
        first_request = await self.__first_request()
        debug_print("KirillVM: " + first_request)
        data_for_named = self.__NAMED_STATE.get_data_for_named()
        match data_for_named.get_enum_data_for_named():
            case EnumDataForKirillVM.EXCEPTION:
                return await callback_w_exception(data_for_named.exception_controller.get_key_parameter_exception())
            case EnumDataForKirillVM.SUCCESS:
                return await callback_w_success(data_for_named.list_task.get_str_where_name_by_task_parameter_list_model())
    
    def dispose(self) -> None:
        self.__NAMED_STATE.dispose()
         
    async def __first_request(self) -> str:
        get_list_task_parameter_one = await self.__TASK_REPOSITORY.get_list_task_parameter_one()
        if get_list_task_parameter_one.EXCEPTION_CONTROLLER.is_where_not_equals_null_parameter_exception():
            return self.__first_qq_first_request_qq_get_list_task_parameter_one(get_list_task_parameter_one.EXCEPTION_CONTROLLER)
        self.__NAMED_STATE.get_data_for_named().list_task = get_list_task_parameter_one.PARAMETER.get_clone()
        return ReadyDataUtility.SUCCESS
    
    def __first_qq_first_request_qq_get_list_task_parameter_one(self, exception_controller: ExceptionController) -> str:
        self.__NAMED_STATE.get_data_for_named().exception_controller = exception_controller
        return exception_controller.get_key_parameter_exception()
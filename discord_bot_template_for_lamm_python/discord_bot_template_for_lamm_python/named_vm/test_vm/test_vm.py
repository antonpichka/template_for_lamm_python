from typing import Callable, final
from library_architecture_mvvm_modify_python import *
from discord_bot_template_for_lamm_python.model_repository.rating_repository.rating_repository import RatingRepository
from discord_bot_template_for_lamm_python.model_repository.user_repository.user_repository import UserRepository
from discord_bot_template_for_lamm_python.named_utility.ready_data_utility import ReadyDataUtility
from discord_bot_template_for_lamm_python.model.rating.rating import Rating
from discord_bot_template_for_lamm_python.named_vm.test_vm.data_for_test_vm import DataForTestVM
from discord_bot_template_for_lamm_python.named_vm.test_vm.enum_data_for_test_vm import EnumDataForTestVM

@final
class TestVM():
    def __init__(self, discord_id: int) -> None:
        ## ModelRepository
        self.__USER_REPOSITORY: UserRepository = UserRepository(EnumRWTMode.TEST)
        self.__RATING_REPOSITORY: RatingRepository = RatingRepository(EnumRWTMode.TEST)

        ## NamedUtility

        ## NamedState
        self.__NAMED_STATE: BaseNamedState[DataForTestVM] = DefaultState[DataForTestVM](DataForTestVM(False,discord_id,Rating("",0)))
    
    async def init_w_build(self, callback_w_exception: Callable[[str], None], callback_w_success: Callable[[str], None]) -> None:
        first_request = await self.__first_request()
        debug_print("TestVM: " + first_request)
        data_for_named = self.__NAMED_STATE.get_data_for_named()
        match data_for_named.get_enum_data_for_named():
            case EnumDataForTestVM.EXCEPTION:
                return await callback_w_exception(data_for_named.exception_controller.get_key_parameter_exception())
            case EnumDataForTestVM.SUCCESS:
                return await callback_w_success(data_for_named.rating.get_str_parameter_elo())

    def dispose(self) -> None:
        self.__NAMED_STATE.dispose()
         
    async def __first_request(self) -> str:
        get_user_from_discord_id_parameter_one = await self.__USER_REPOSITORY.get_user_from_discord_id_parameter_one(self.__NAMED_STATE.get_data_for_named().DISCORD_ID)
        if get_user_from_discord_id_parameter_one.EXCEPTION_CONTROLLER.is_where_not_equals_null_parameter_exception():
            return self.__first_qq_first_request_qq_get_user_from_discord_id_parameter_one(get_user_from_discord_id_parameter_one.EXCEPTION_CONTROLLER)
        get_rating_from_unique_id_by_user_parameter_one = await self.__RATING_REPOSITORY.get_rating_from_unique_id_by_user_parameter_one(get_user_from_discord_id_parameter_one.PARAMETER.UNIQUE_ID)
        if get_rating_from_unique_id_by_user_parameter_one.EXCEPTION_CONTROLLER.is_where_not_equals_null_parameter_exception():
            return self.__first_qq_first_request_qq_get_rating_from_unique_id_by_user_parameter_one(get_rating_from_unique_id_by_user_parameter_one.EXCEPTION_CONTROLLER)
        self.__NAMED_STATE.get_data_for_named().rating = get_rating_from_unique_id_by_user_parameter_one.PARAMETER.get_clone()
        return ReadyDataUtility.SUCCESS
    
    def __first_qq_first_request_qq_get_user_from_discord_id_parameter_one(self, exception_controller: ExceptionController) -> str:
        self.__NAMED_STATE.get_data_for_named().exception_controller = exception_controller
        return exception_controller.get_key_parameter_exception()
    
    def __first_qq_first_request_qq_get_rating_from_unique_id_by_user_parameter_one(self, exception_controller: ExceptionController) -> str:
        self.__NAMED_STATE.get_data_for_named().exception_controller = exception_controller
        return exception_controller.get_key_parameter_exception()
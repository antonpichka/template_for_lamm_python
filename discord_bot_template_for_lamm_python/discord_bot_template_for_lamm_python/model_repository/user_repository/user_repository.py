import asyncio
from typing import Generic, TypeVar
from library_architecture_mvvm_modify_python import *
from discord_bot_template_for_lamm_python.model.user.list_user import ListUser
from discord_bot_template_for_lamm_python.model.user.user import User

T = TypeVar("T", bound=User)
Y = TypeVar("Y", bound=ListUser)

class UserRepository(Generic[T,Y], BaseModelRepository[T,Y]):
    def __init__(self, enum_rwt_mode: EnumRWTMode) -> None:
        super().__init__(enum_rwt_mode)

    def _get_base_model_from_map_and_list_keys(self, map: dict[str, object], list_keys: list[str]) -> T:
        return User(
            self._get_safe_value_where_used_in_method_get_model_from_map_and_list_keys_and_index_and_default_value(
                map, list_keys, 0, ""),
            self._get_safe_value_where_used_in_method_get_model_from_map_and_list_keys_and_index_and_default_value(
                map, list_keys, 1, 0))
    
    def _get_base_list_model_from_list_model(self, list_model: list[T]) -> Y:
        return ListUser(list_model)
    
    async def get_user_from_discord_id_parameter_one(self, discord_id: int) -> Result:
        return await self._get_mode_callback_from_release_callback_and_test_callback_parameter_enum_rwt_mode(
            self._get_user_from_discord_id_parameter_one_w_release_callback,
            self._get_user_from_discord_id_parameter_one_w_test_callback)(discord_id)
    
    async def _get_user_from_discord_id_parameter_one_w_release_callback(self,discord_id: int) -> Result:
        raise LocalException("UserRepository",EnumGuilty.DEVELOPER,"UserRepositoryQQGet_user_from_discord_id_parameter_one_w_release_callback")
    
    async def _get_user_from_discord_id_parameter_one_w_test_callback(self, discord_id: int) -> Result:
        await asyncio.sleep(1)
        return Result.success(self._get_base_model_from_map_and_list_keys(
            {
                "uniqueId" : "19593a8a-e8ad-42c0-a4ff-aedc42005570",
                "discordId" : discord_id
            },
            self._get_user_from_discord_id_parameter_one_w_list_keys()))
    
    def _get_user_from_discord_id_parameter_one_w_list_keys(self) -> list[str]:
        return ["uniqueId","discordId"]

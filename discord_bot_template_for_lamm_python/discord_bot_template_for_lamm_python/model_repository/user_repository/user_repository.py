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
        if len(list_keys) <= 0:
            return User("",0)
        if map.get(list_keys[0]) is None:
            return User("",0)
        if len(list_keys) <= 1:
            return User(map.get(list_keys[0]),0)
        if map.get(list_keys[1]) is None:
            return User(map.get(list_keys[0]),0)
        return User(map.get(list_keys[0]),map.get(list_keys[1]))
    
    def _get_base_list_model_from_list_model(self, list_model: list[T]) -> Y:
        return ListUser(list_model)
    
    async def get_user_from_discord_id_parameter_one(self, discord_id: int) -> Result:
        return await self._get_mode_callback_from_release_callback_and_test_callback_parameter_enum_rwt_mode(
            self.__get_user_from_discord_id_parameter_one_w_release_callback,
            self.__get_user_from_discord_id_parameter_one_w_test_callback)(discord_id)
    
    async def __get_user_from_discord_id_parameter_one_w_release_callback(self,discord_id: int) -> Result:
        raise LocalException("UserRepository",EnumGuilty.DEVELOPER,"UserRepositoryQQGet_user_from_discord_id_parameter_one_w_release_callback")
    
    async def __get_user_from_discord_id_parameter_one_w_test_callback(self, discord_id: int) -> Result:
        await asyncio.sleep(1)
        return Result.success(self._get_base_model_from_map_and_list_keys(
            {
                "uniqueId" : "19593a8a-e8ad-42c0-a4ff-aedc42005570",
                "discordId" : discord_id
            },
            ["uniqueId","discordId"]))

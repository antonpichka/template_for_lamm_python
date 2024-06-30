import asyncio
from typing import Generic, TypeVar
from library_architecture_mvvm_modify_python import *
from discord_bot_template_for_lamm_python.model.rating.list_rating import ListRating
from discord_bot_template_for_lamm_python.model.rating.rating import Rating

T = TypeVar("T", bound=Rating)
Y = TypeVar("Y", bound=ListRating)

class RatingRepository(Generic[T,Y], BaseModelRepository[T,Y]):
    def __init__(self, enum_rwt_mode: EnumRWTMode) -> None:
        super().__init__(enum_rwt_mode)

    def _get_base_model_from_map_and_list_keys(self, map: dict[str, object], list_keys: list[str]) -> T:
        return Rating(
            self._get_safe_value_where_used_in_method_get_model_from_map_and_list_keys_and_index_and_default_value(
                map, list_keys, 0, ""),
            self._get_safe_value_where_used_in_method_get_model_from_map_and_list_keys_and_index_and_default_value(
                map, list_keys, 1, 0))
    
    def _get_base_list_model_from_list_model(self, list_model: list[T]) -> Y:
        return ListRating(list_model)
    
    async def get_rating_from_unique_id_by_user_parameter_one(self, unique_id_by_user: str) -> Result:
        return await self._get_mode_callback_from_release_callback_and_test_callback_parameter_enum_rwt_mode(
            self._get_rating_from_unique_id_by_user_parameter_one_w_release_callback,
            self._get_rating_from_unique_id_by_user_parameter_one_w_test_callback)(unique_id_by_user)
    
    async def _get_rating_from_unique_id_by_user_parameter_one_w_release_callback(self, unique_id_by_user: str) -> Result:
        raise LocalException("RatingRepository",EnumGuilty.DEVELOPER,"RatingRepositoryQQGet_rating_from_unique_id_by_user_parameter_one_w_release_callback")
    
    async def _get_rating_from_unique_id_by_user_parameter_one_w_test_callback(self, unique_id_by_user: str) -> Result:
        await asyncio.sleep(1)
        return Result.success(self._get_base_model_from_map_and_list_keys(
            {
                "uniqueIdByUser" : unique_id_by_user,
                "elo" : 322
            },
            self._get_rating_from_unique_id_by_user_parameter_one_w_list_keys()
        ))
    
    def _get_rating_from_unique_id_by_user_parameter_one_w_list_keys(self) -> list[str]:
        return ["uniqueIdByUser","elo"]


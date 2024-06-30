from typing import Generic, TypeVar
from library_architecture_mvvm_modify_python import *
from discord_bot_template_for_lamm_python.model.example.example import Example
from discord_bot_template_for_lamm_python.model.example.list_example import ListExample

T = TypeVar("T", bound=Example)
Y = TypeVar("Y", bound=ListExample)

class ExampleRepository(Generic[T,Y], BaseModelRepository[T,Y]):
    def __init__(self) -> None:
        super().__init__()

    def _get_base_model_from_map_and_list_keys(self, map: dict[str, object], list_keys: list[str]) -> T:
        return Example(
            self._get_safe_value_where_used_in_method_get_model_from_map_and_list_keys_and_index_and_default_value(
                map, list_keys, 0, ""))
    
    def _get_base_list_model_from_list_model(self, list_model: list[T]) -> Y:
        return ListExample(list_model)
    
    async def get_example_parameter_one(self) -> Result:
        return await self._get_mode_callback_from_release_callback_and_test_callback_parameter_enum_rwt_mode(
            self._get_example_parameter_one_w_release_callback,
            self._get_example_parameter_one_w_test_callback)()
    
    async def _get_example_parameter_one_w_release_callback(self) -> Result:
        raise LocalException("ExampleRepository",EnumGuilty.DEVELOPER,"ExampleRepositoryQQGet_example_parameter_one_w_release_callback")
    
    async def _get_example_parameter_one_w_test_callback(self) -> Result:
        raise LocalException("ExampleRepository",EnumGuilty.DEVELOPER,"ExampleRepositoryQQGet_example_parameter_one_w_test_callback")

    def _get_example_parameter_one_w_list_keys(self) -> list[str]:
        raise LocalException("ExampleRepository",EnumGuilty.DEVELOPER,"ExampleRepositoryQQGet_example_parameter_one_w_list_keys")
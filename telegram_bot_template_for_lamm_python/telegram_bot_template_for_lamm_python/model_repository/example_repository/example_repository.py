from typing import Generic, TypeVar
from library_architecture_mvvm_modify_python import *
from telegram_bot_template_for_lamm_python.model.example.example import Example
from telegram_bot_template_for_lamm_python.model.example.list_example import ListExample

T = TypeVar("T", bound=Example)
Y = TypeVar("Y", bound=ListExample)

class ExampleRepository(Generic[T,Y], BaseModelRepository[T,Y]):
    def __init__(self, enum_rwt_mode: EnumRWTMode) -> None:
        super().__init__(enum_rwt_mode)

    def _get_base_model_from_map_and_list_keys(self, map: dict[str, object], list_keys: list[str]) -> T:
        if len(list_keys) <= 0:
            return Example("")
        if map.get(list_keys[0]) is None:
            return Example("")
        return Example(map.get(list_keys[0]))
    
    def _get_base_list_model_from_list_model(self, list_model: list[T]) -> Y:
        return ListExample(list_model)
    
    async def get_example_parameter_qwe_service(self) -> Result:
        return await self._get_mode_callback_from_release_callback_and_test_callback_parameter_enum_rwt_mode(
            self.__get_example_parameter_qwe_service_w_release_callback,
            self.__get_example_parameter_qwe_service_w_test_callback)()
    
    async def __get_example_parameter_qwe_service_w_release_callback(self) -> Result:
        raise LocalException("ExampleRepository",EnumGuilty.DEVELOPER,"ExampleRepositoryQQGet_example_parameter_qwe_service_w_release_callback")
    
    async def __get_example_parameter_qwe_service_w_test_callback(self) -> Result:
        raise LocalException("ExampleRepository",EnumGuilty.DEVELOPER,"ExampleRepositoryQQGet_example_parameter_qwe_service_w_test_callback")

import asyncio
from typing import Generic, TypeVar
from library_architecture_mvvm_modify_python import *
from discord_bot_template_for_lamm_python.model.task.task import Task
from discord_bot_template_for_lamm_python.model.task.list_task import ListTask

T = TypeVar("T", bound=Task)
Y = TypeVar("Y", bound=ListTask)

class TaskRepository(Generic[T,Y], BaseModelRepository[T,Y]):
    def __init__(self, enum_rwt_mode: EnumRWTMode) -> None:
        super().__init__(enum_rwt_mode)

    def _get_base_model_from_map_and_list_keys(self, map: dict[str, object], list_keys: list[str]) -> T:
        if len(list_keys) <= 0:
            return Task("","")
        if map.get(list_keys[0]) is None:
            return Task("","")
        if len(list_keys) <= 1:
            return Task(map.get(list_keys[0]),"")
        if map.get(list_keys[1]) is None:
            return Task(map.get(list_keys[0]),"")
        return Task(map.get(list_keys[0]),map.get(list_keys[1]))
    
    def _get_base_list_model_from_list_model(self, list_model: list[T]) -> Y:
        return ListTask(list_model)
    
    async def get_list_task_parameter_one(self) -> Result:
        return await self._get_mode_callback_from_release_callback_and_test_callback_parameter_enum_rwt_mode(
            self.__get_list_task_parameter_one_w_release_callback,
            self.__get_list_task_parameter_one_w_test_callback)()
    
    async def __get_list_task_parameter_one_w_release_callback(self) -> Result:
        raise LocalException("TaskRepository",EnumGuilty.DEVELOPER,"TaskRepositoryQQGet_list_task_parameter_one_w_release_callback")
    
    async def __get_list_task_parameter_one_w_test_callback(self) -> Result:
        map: dict[str, list[dict[str, object]]] = {
            "tasks": [
                {
                    "uniqueId" : "be6096e7-7fc8-423f-b84a-d95c07387b0b",
                    "name" : "Brush your teeth"
                },
                {
                    "uniqueId" : "785e8d87-df1b-491c-bcb0-0005a374658a",
                    "name" : "Do a workout"
                },
                {
                    "uniqueId" : "133d5f2f-f3dc-4819-ad49-b84b254e077e",
                    "name" : "Eat"
                },
                {
                    "uniqueId" : "14b9a2de-082a-4b95-a154-096d9526ddc4",
                    "name" : "Sleep"
                }
            ]
        }
        list_model = list[T]()
        tasks = map.get("tasks")
        for task in tasks:
            list_model.append(self._get_base_model_from_map_and_list_keys(
                task,
                ["uniqueId","name"]))
        await asyncio.sleep(1)
        return Result.success(self._get_base_list_model_from_list_model(list_model))
        
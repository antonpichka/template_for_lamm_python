import asyncio
from discord.ext import commands
from typing import final
from library_architecture_mvvm_modify_python import BaseNamedState, DefaultState, RWTMode, EnumRWTMode, NamedCallback, debug_print
from discord_bot_template_for_lamm_python.src.named_utility.keys_success_utility import KeysSuccessUtility
from discord_bot_template_for_lamm_python.src.named_vm.kirill_vm.data_for_kirill_vm import DataForKirillVM
from discord_bot_template_for_lamm_python.src.named_vm.kirill_vm.enum_data_for_kirill_vm import EnumDataForKirillVM

@final
class KirillVM():
    def __init__(self) -> None:
        ## OperationEEModel(EEWhereNamed)[EEFromNamed]EEParameterNamedService
        ## NamedUtility

        ## Main objects 
        self.__NAMED_STATE: BaseNamedState[DataForKirillVM] = DefaultState[DataForKirillVM](DataForKirillVM(False))
        self.__RWT_MODE: RWTMode = RWTMode(
            EnumRWTMode.TEST,
            [
                NamedCallback("init",self.__init_release_callback)
            ],
            [
                NamedCallback("init",self.__init_test_callback)
            ]
        )
    
    async def initWBuild(self, ctx: commands.Context, bot: commands.Bot) -> None:
        callback = await self.__RWT_MODE.get_named_callback_from_name("init").CALLBACK()
        debug_print("KirillVM: " + callback)
        data_for_named = self.__NAMED_STATE.get_data_for_named()
        match data_for_named.get_enum_data_for_named():
            case EnumDataForKirillVM.EXCEPTION:
                channel = bot.get_channel(receiving_channel_id)
                await channel.send("TASK")
                return
            case EnumDataForKirillVM.SUCCESS:
                await channel.send("TASK")
                return
            case _:
                return
    
    def dispose(self) -> None:
        self.__NAMED_STATE.dispose()

    async def __init_release_callback(self) -> str:
        await asyncio.sleep(1)
        return KeysSuccessUtility.SUCCESS
         
    async def __init_test_callback(self) -> str:
        return KeysSuccessUtility.SUCCESS
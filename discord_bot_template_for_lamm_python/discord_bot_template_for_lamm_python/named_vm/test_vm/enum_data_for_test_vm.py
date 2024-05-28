from enum import Enum
from typing import final

@final
class EnumDataForTestVM(Enum):
    EXCEPTION = "exception"
    SUCCESS = "success"
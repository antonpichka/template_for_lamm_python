from enum import Enum
from typing import final

@final
class EnumDataForExampleVM(Enum):
    EXCEPTION = "exception"
    SUCCESS = "success"
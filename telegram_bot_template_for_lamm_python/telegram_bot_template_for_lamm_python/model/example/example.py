from library_architecture_mvvm_modify_python import *

class Example(BaseModel):
    def __init__(self, unique_id: str) -> None:
        super().__init__(unique_id)
    
    def get_clone(self) -> 'Example':
        return Example(self.UNIQUE_ID)
    
    def to_string(self) -> str:
        return "Example(unique_id: " + self.UNIQUE_ID + ")"
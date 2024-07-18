from library_architecture_mvvm_modify_python import *

class Task(BaseModel):
    def __init__(self, unique_id: str, name: str) -> None:
        super().__init__(unique_id)
        self.NAME: str = name
    
    def get_clone(self) -> 'Task':
        return Task(self.UNIQUE_ID,self.NAME)
    
    def to_string(self) -> str:
        return "Task(unique_id: " + self.UNIQUE_ID + ", name: " + self.NAME + ")"
from library_architecture_mvvm_modify_python import *

class User(BaseModel):
    def __init__(self, unique_id: str, discord_id: int) -> None:
        super().__init__(unique_id)
        self.DISCORD_ID: int = discord_id
    
    def get_clone(self) -> 'User':
        return User(self.UNIQUE_ID, self.DISCORD_ID)
    
    def to_string(self) -> str:
        return "User(unique_id: " + self.UNIQUE_ID + ", discord_id: " + str(self.DISCORD_ID) + ")"
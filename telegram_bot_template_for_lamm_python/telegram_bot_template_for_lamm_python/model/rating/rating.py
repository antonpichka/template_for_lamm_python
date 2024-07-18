from library_architecture_mvvm_modify_python import *

class Rating(BaseModel):
    def __init__(self, unique_id_by_user: str, elo: int) -> None:
        super().__init__(unique_id_by_user)
        self.UNIQUE_ID_BY_USER: str = unique_id_by_user
        self.ELO: int = elo
    
    def get_clone(self) -> 'Rating':
        return Rating(self.UNIQUE_ID_BY_USER, self.ELO)
    
    def to_string(self) -> str:
        return "Rating(unique_id_by_user: " + self.UNIQUE_ID_BY_USER + ", elo: " + str(self.ELO) + ")"

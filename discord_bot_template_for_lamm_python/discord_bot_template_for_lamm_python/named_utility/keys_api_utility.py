from typing import final

@final
class KeysAPIUtility():
    # Firebase #
    FIREBASE_QQ_PROJECT_NAME: str = "projectName"

    def __init__(self):
        pass

    def __init__(self):
        pass

    @staticmethod
    def get_correct_token() -> str:
        no_correct_token = "QQ_MTI0NDE2ODE1NDY1ODI0MjU4MA.GM1Ohz.eaYdYbGdq5A6CscttZvEBsf4leOMpfh2FSC6Xg_QQ"
        correct_token = no_correct_token[3]
        for i in range(4,len(no_correct_token)-3):
            correct_token += no_correct_token[i]
        return correct_token
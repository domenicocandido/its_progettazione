class Nazione:
    
    _nome:str

    def __init__(self, nome:str):

        self._nome = nome


    def get_nome(self) -> str:
        return self._nome

    def set_nome(self, nome:str) -> None:
        self._nome = nome

import custom_types



class Facoltà:

    _nome: str
    _tipo_facoltà: str

    def __init__(self, nome:str, tipo_facoltà:str):

        self._nome = nome
        self._tipo_facoltà= tipo_facoltà
    
    def get_nome(self) -> str:
        return self._nome
    
    def set_nome(self, nuovo_nome:str) -> None:
        self._nome = nuovo_nome

    def get_tipo_facoltà(self) -> str:
        return self._tipo_facoltà
    
    def set_tipo_facoltà(self, nuova_facoltà:str) -> None:
        self._tipo_facoltà = nuova_facoltà
        
        
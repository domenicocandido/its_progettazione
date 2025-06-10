from custom_types import RealGTZ
from facoltà import Facoltà

class Corso:

    _nome:str
    _codice:str
    _durata_ore:RealGTZ
    _appartiene:Facoltà

    def __init__(self, nome:str, codice:str, durata_ore:RealGTZ, appartiene:Facoltà):
        
        self._nome = nome
        self._codice = codice
        self._durata_ore = durata_ore
        self.set_appartiene(appartiene)

    def get_nome(self) -> str:
        return self._nome
    
    def set_nome(self, nuovo_nome:str) -> None:
        self._nome = nuovo_nome

    def get_codice(self) -> str:
        return self._codice
    
    def set_codice(self, nuovo_codice:str) -> None:
        self._codice = nuovo_codice

    def get_durata_ore(self) -> RealGTZ:
        return self.__durata_ore
    
    def set_durata_ore(self, nuova_durata:RealGTZ) -> None:
        self.__durata_ore = nuova_durata

    def get_appartiene(self) -> Facoltà:
        return self._appartiene
    
    def set_appartiene(self, appartiene:Facoltà) -> None:
        self._appartiene = appartiene
    

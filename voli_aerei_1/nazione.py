from typing import List
from città import Citta


class Nazione:
    
    _nome:str
    _citta: List[Citta]

    def __init__(self, nome:str):

        self._nome = nome
        self._citta = []

    def get_nome(self) -> str:
        return self._nome

    def set_nome(self, nuovo_nome:str) -> None:
        self._nome = nuovo_nome

    def get_citta(self) -> Citta:
        return self._citta
    
    def aggiungi_citta(self, citta: Citta) -> None:
        self._citta.append(citta)
    
    def rimuovi_citta(self, citta: Citta) -> None:
        self._citta.remove(citta)
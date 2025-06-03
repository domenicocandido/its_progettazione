from typing import List
from volo import Volo
from città import *

class Aereoporto:

    _codice:str
    _nome:str
    _citta: Citta
    _voli:List[Volo]

    def __init__(self, codice:str, nome:str, citta:Citta) -> None:

        self._codice = codice
        self._nome = nome
        self._citta = citta
        self._voli = []

    def get_codice(self) -> str:
        return self._codice

    def get_nome(self) -> str:
        return self._nome
    
    def set_nome(self, nuovo_nome:str) -> None:
        self._nome = nuovo_nome
    
    def get_citta(self) -> Citta:
        return self._citta
    
    def set_citta(self, nuova_citta:Citta) -> None:
        self._citta = nuova_citta
    
    def get_voli(self) -> List[Volo]:
        return self._voli
    
    def aggiungi_volo (self, volo:Volo) -> None:
        self._voli.append(volo)

    def rimuovi_volo (self, volo:Volo) -> None:
        self._voli.remove(volo)


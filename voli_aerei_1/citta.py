from custom_types import RealGEZ
from nazione import Nazione
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from compagnia import Compagnia
    from aeroporto import Aeroporto

class Citta:

    _nome: str
    _abitanti: RealGEZ
    _nazione: Nazione
    _compagnie: List["Compagnia"]
    _aeroporti: List["Aeroporto"]

    def __init__(self, nome: str, abitanti: RealGEZ, nazione: Nazione) -> None:
        self._nome = nome
        self.set_abitanti(abitanti)
        self._nazione = nazione
        self._compagnie = []
        self._aeroporti = []

    def get_nome(self) -> str:
        return self._nome
    
    def set_nome(self, nuovo_nome: str) -> None:
        self._nome = nuovo_nome

    def get_abitanti(self) -> RealGEZ:
        return self._abitanti

    def set_abitanti(self, nuovi_abitanti: RealGEZ) -> None:
        if nuovi_abitanti < 0:
            raise ValueError("Il numero di abitanti deve essere >= 0")
        self._abitanti = nuovi_abitanti

    def get_nazione(self) -> Nazione:
        return self._nazione
    
    def set_nazione(self, nuova_nazione: Nazione) -> None:
        self._nazione = nuova_nazione

    def get_compagnie(self) -> List["Compagnia"]:
        return self._compagnie

    def aggiungi_compagnia(self, compagnia: "Compagnia") -> None:
        self._compagnie.append(compagnia)

    def rimuovi_compagnia(self, compagnia: "Compagnia") -> None:
        if compagnia in self._compagnie:
            self._compagnie.remove(compagnia)

    def get_aeroporti(self) -> List["Aeroporto"]:
        return self._aeroporti

    def aggiungi_aeroporto(self, aeroporto: "Aeroporto") -> None:
        self._aeroporti.append(aeroporto)

    def rimuovi_aeroporto(self, aeroporto: "Aeroporto") -> None:
        if aeroporto in self._aeroporti:
            self._aeroporti.remove(aeroporto)

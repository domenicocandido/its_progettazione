from custom_types import RealGTZ
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from compagnia import Compagnia
    from aeroporto import Aeroporto

class Volo:

    _codice: str
    _durata_min: RealGTZ
    _compagnia: "Compagnia"
    _partenza: "Aeroporto" 
    _arrivo: "Aeroporto"

    def __init__(self, codice:str, durata_min:  RealGTZ, compagnia: "Compagnia", partenza: "Aeroporto", arrivo: "Aeroporto") -> None:

        self._codice = codice
        self._durata_min = durata_min
        self._compagnia = compagnia
        self._arrivo = arrivo
        self._partenza = partenza


    def get_codice(self) -> str:
        return self._codice
    
    def set_codice(self, nuovo_codice:str) -> None:
        self._codice = nuovo_codice

    def get_durata_min(self) -> RealGTZ:
        return self._durata_min
    
    def set_durata(self, nuova_durata: RealGTZ) -> None:
    
        if nuova_durata <= 0:
            raise ValueError("La durata del volo deve essere maggiore di  0.")
        self._durata_min = nuova_durata

    def get_compagnia(self) -> "Compagnia":
        return self._compagnia
    
    def set_compagnia(self, compagnia:"Compagnia") -> None:
        self._compagnia = compagnia

    def get_arrivo(self) -> "Aeroporto":
        return self._arrivo
    
    def get_partenza(self) -> "Aeroporto":
        return self._partenza
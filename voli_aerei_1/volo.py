from datetime import date
from custom_types import RealGTZ
from compagnia import Compagnia

class Volo:

    _codice: str
    _durata_min: RealGTZ
    _compagnia: Compagnia

    def __init__(self, codice:str, durata_min:  RealGTZ, compagnia: Compagnia) -> None:

        self._codice = codice
        self._durata_min = durata_min
        self._compagnia = compagnia

    def get_codice(self) -> str:
        return self._codice
    
    def set_codice(self, nuovo_codice:str) -> None:
        self._codice = nuovo_codice

    def get_durata_min(self) -> RealGTZ:
        return self._durata_min
    
    def set_durata_min(self, nuova_durata: RealGTZ) -> None:
    
        if nuova_durata <= 0:
            raise ValueError("La durata del volo deve essere maggiore di  0.")
        self._durata_min = nuova_durata

    def get_compagnia(self) -> Compagnia:
        return self._compagnia
    
    def set_compagnia(self, nuova_compagnia:Compagnia) -> None:
        self._compagnia = nuova_compagnia
from custom_types import RealGEZ
from typing import TYPE_CHECKING
from datetime import date

if TYPE_CHECKING:
    from impiegato import Impiegato

class Progetto:

    _nome:str
    _budget:RealGEZ
    _impiegati: list['Progetto']

    def __init__ (self, nome:str, budget.RealGEZ):
        self._nome = nome
        self._budget = budget
        self._impiegato = []

    def get_nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome:str) -> None:
        self._nome = nome

    def get_budget(self) -> RealGEZ:
        return self._budget
    
    def set_budget(self, budget:RealGEZ) -> None:
        self._budget = budget

    def add_impiegato(self, impiegato:'Impiegato', data:date) -> None:

        self._data = data
        self._impiegato = 'Impiegato'

        if impiegato in self._impiegati:
            self._impiegati.append(impiegato)
        else:
            print("L'impiegato è già coinvolto nel progetto.")

    def remove_impiegato(self, impiegato:'Impiegato') -> None:

        if len(self._impiegati) == 0:
            raise ValueError("Non ci sono impiegati nel progetto.")
        else:

            if impiegato in self._impiegati:
                self._impiegati.remove(impiegato)
            else:
                print("L'impiegato non è coinvolto nel progetto.") 


    def get_impiegati(self) -> list['Impiegato']:
        return self._impiegati
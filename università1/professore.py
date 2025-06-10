from datetime import date
from custom_types import CodiceFiscale
from corso import Corso

class Professore:

    _nome:str
    _data_nascita:date # <<immu>>
    _cod_fiscale:CodiceFiscale # <<immu>>
    _insegna:Corso

    def __init__(self, nome:str, data_nascita:date, cod_fiscale: CodiceFiscale, insegna:Corso):
        self._nome =  nome
        self._data_nascita= data_nascita
        self._cod_fiscale = cod_fiscale
        self.set_insegna(insegna)

    def get_nome(self) -> str:
        return self._nome
    
    def set_nome(self, nuovo_nome:str) -> None:
        self._nome = nuovo_nome

    def get_data_nascita(self) -> date:
        return self._data_nascita
    
    def get_cod_fiscale(self) -> CodiceFiscale:
        return self._cod_fiscale
    
    def get_insegna(self) -> Corso:
        return self._insegna
    
    def set_insegna(self, insegna:Corso) -> None:
        self._insegna = insegna



from custom_types import RealGTZ, CodiceFiscale
from datetime import date
from corso import Corso

class Studente:

    _nome:str
    _cod_fiscale:CodiceFiscale
    _data_nascita:date
    _anno_iscrizione:RealGTZ
    _num_matricola:RealGTZ
    _corsi_superati: dict[Corso, RealGTZ]
    _voto:RealGTZ
    _iscritto:Corso


    def __init__(self, nome:str, cod_fiscale:CodiceFiscale, data_nascita:date, anno_iscrizione:RealGTZ, num_matricola:RealGTZ, corsi_superati:dict[Corso, RealGTZ], voto:RealGTZ, iscritto:Corso):
        self._nome = nome
        self._cod_fiscale =  cod_fiscale
        self._data_nascita = data_nascita
        self._anno_iscrizione = anno_iscrizione
        self._num_matricola = num_matricola
        self._corsi_superati = corsi_superati
        self._voto = voto
        self.set_iscritto(iscritto)

    def get_nome(self) -> str:
        return self._nome
    
    def set_nome(self, nuovo_nome:str) -> None:
        self._nome = nuovo_nome

    def get_cod_fiscale(self) -> CodiceFiscale:
        return self._cod_fiscale
    
    def get_data_nascita(self) -> date:
        return self._data_nascita
    
    def get_anno_iscrizione(self) -> RealGTZ:
        return self._anno_iscrizione
    
    def get_num_matricola(self) -> RealGTZ:
        return self._num_matricola
    
    def get_corsi_superati(self) -> dict[Corso,RealGTZ]:

        if self._corsi_superati:
            return self._corsi_superati
        else:
            print("Non ci sono corsi superati")

    def set_corsi_superati(self, nuovo_corso_superato:Corso, voto:RealGTZ) -> None:

        if 18 <= self._voto <= 30:
            self._corsi_superati[nuovo_corso_superato] = voto
        else:
            raise ValueError("Il voto non è valido!")

    def get_iscritto(self) -> Corso:
        return self._iscritto
    
    def set_iscritto(self, iscritto:Corso) -> None:
        self._iscritto = iscritto

            



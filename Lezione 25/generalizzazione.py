from datetime import date
from abc import ABC, abstractmethod
class Persona:

    _nome:str
    
    @abstractmethod
    def __init__(self, nome:str):
        self._nome = nome

    def getNome(self) -> str:
        return self._nome
    
    def setNome(self, nome:str) -> None:
        self._nome = nome
    
class Docente(Persona):

    _data_nascita:date
    
    def __init__(self, nome:str, data_nascita:date):
        self._data_nascita = data_nascita

    def getNome(self) -> date:
        return self._data_nascita
    
    def setNome(self, data_nascita:str) -> None:
        self._data_nascita = data_nascita

class Studente(Persona):

    _matricola:int
    
    def __init__(self, matricola:int):
        self._matricola = matricola

    def getMatricola(self) -> int:
        return self._matricola
    
    def setMAtricola(self, matricola:int) -> None:
        self._matricola = matricola
    
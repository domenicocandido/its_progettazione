from __future__ import annotations
from custom_types import *


class Persona:
    _nome: str
    _cognome: str
    _cf: list[CodiceFiscale] # [1..*]
    _genere: Genere
    _maternita: IntGEZ # [0..1] - deve avere un valore se e solo se _genere = Genere.donna
    _posizione_mil: PosizioneMilitare | None # [0..1] da aggregazione, deve avere un valore se e solo se _genere = Genere.uomo
    _is_impiegato: bool
    _is_studente: bool

    def __init__(self, *, nome: str, cognome: str,
                 cf: list[CodiceFiscale],
                 genere: Genere,
                 maternita: IntGEZ|None=None,
                 is_studente:bool, 
                 is_impiegato:bool,
                 posizione_mil:PosizioneMilitare) -> None:
        self._nome = nome
        self._cognome = cognome
        self._genere = genere

        if not cf:
            raise ValueError("La persona deve avere almeno un codice fiscale!")
        if is_studente and is_impiegato:
            raise ValueError("Una persona non può essere sia studente che impiegato")
        if genere == Genere.donna:
            if maternita is None:
                raise ValueError("È obbligatorio fornire il numero di maternità per le donne")
            self.set_maternita(maternita)
            self._posizione_mil = None

        if genere == Genere.uomo:
            if posizione_mil is None:
                raise ValueError("Un uomo deve avere una posizione militare.")
            self._posizione_mil = posizione_mil
        self._is_studente = is_studente
        self._is_impiegato = is_impiegato



    def diventa_donna(self, maternita: IntGEZ) -> None:
        if self._genere == Genere.donna:
            raise RuntimeError("La persona era già una donna!")
        self._genere = Genere.donna
        self.set_maternita(maternita)
        self.__dimentica_uomo()

    def __dimentica_uomo(self) -> None:
        # Questo metodo è privato perché non deve essere mai invocato dall'esterno, ma solo all'interno di questa classe
        self._posizione_mil = None

    def set_maternita(self, maternita: IntGEZ) -> None:
        if not self._genere == Genere.donna:
            raise RuntimeError("Gli uomini non hanno il numero di maternità!")
        self._maternita = maternita


class Impiegato(Persona):

    def __init__(self, *, nome, cognome, cf, genere, maternita=None, posizione_mil:PosizioneMilitare, stipendio: RealGEZ, ruolo: Ruolo, is_responsabile: bool):
        super().__init__(
            nome=nome,
            cognome=cognome,
            cf=cf,
            genere=genere,
            maternita=maternita,
            is_impiegato=True, 
            is_studente=False,
            posizione_mil = posizione_mil
        )

        self._stipendio = stipendio
        self._ruolo = ruolo
        self._is_responsabile = is_responsabile

        if ruolo == Ruolo.progettista:
            if is_responsabile:
                print("L'impiegato partecipa al progetto come responsabile.")
            else:
                print("L'impiegato non è il responsabile del progetto.")
        else:
            raise ValueError("L'impiegato non è un progettista")
        
        if self._is_impiegato == True:
            self._is_studente = False
        
        
    def getRuolo(self) -> Ruolo:
        return self._ruolo
    
    def getResponsabile(self):
        return self._is_responsabile
    
    def diventaSegretario(self) -> None:
        if self._is_responsabile == False :
            self._ruolo = Ruolo.segretario
        else:
            raise ValueError("Un responsabile non può diventare un segretario")
    
    def diventaDirettore(self) -> None:
        if self._ruolo == Ruolo.progettista and self._is_responsabile == False:
            self._ruolo = Ruolo.direttore
        else:
            raise ValueError("Un responsabile di un progetto non può diventare direttore.")
    
    def diventaProgettista(self) -> None:
        self._ruolo = Ruolo.progettista
    
    def diventaResponsabile(self) -> None:
        if self._ruolo == Ruolo.progettista:
            self._is_responsabile = True
        else:
            self._is_responsabile = False
           

imp = Impiegato( nome="Domenico", cognome="Candido", cf=[CodiceFiscale("CNDDNC05E17I234E")], genere=Genere.uomo, stipendio=RealGEZ(2800.0), ruolo=Ruolo.progettista, is_responsabile=True)


class Studente(Persona):
    _matricola:RealGTZ # immutabile

    def __init__(self, *, nome, cognome, cf, genere, maternita = None, matricola:RealGTZ):
        super().__init__(nome=nome, cognome=cognome, cf=cf, genere=genere, maternita=maternita, is_studente=True, is_impiegato=False)
        self._matricola = matricola

        if not self._is_studente:
            raise ValueError("Solo gli studenti possono avere la matricola")
        else:
            self._matricola = matricola

    def getMatricola(self) -> RealGTZ:
        return self._matricola
    
class Progetto:
    
    _nome:str

    def __init__(self, nome:str):
        self._nome = nome

class PosizioneMilitare:
    
    _nome:str
    
    def __init__(self, nome:str):
        self._nome = nome

    def getNome(self) -> str:
        return self._nome


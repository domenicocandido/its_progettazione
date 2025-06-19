from dipartimento import Dipartimento
from impiegato import Impiegato
from datetime import date

class Afferenza:

    _data_afferenza:date

    def __init__(self, impiegato:Impiegato, dipartimento:Dipartimento, data_afferenza:date):

        self._impiegato = impiegato
        self._dipartimento = dipartimento
        self.set_data_afferenza(data_afferenza)


    def get_impiegato(self) -> Impiegato:
        return self._impiegato
    
    def set_impiegato(self, impiegato:Impiegato) -> None:
        self._impiegato = impiegato

    def get_dipartimento(self) -> Dipartimento:
        return self._dipartimento
    
    def set_dipartimento(self, dipartimento:Dipartimento) -> None:
        self._dipartimento = dipartimento

    def get_data_afferenza(self) -> date:
        return self._data_afferenza
    
    def set_data_afferenza(self, data_afferenza:date) -> None:
        if not isinstance(data_afferenza, date):
            raise ValueError(f"La data di afferenza deve essere di tipo date.")
        self._data_afferenza = data_afferenza




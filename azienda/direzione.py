from impiegato import Impiegato
from dipartimento import Dipartimento

class Direzione:

    class _link:

        _dipartimento:Dipartimento
        _direttore:Impiegato

        def __init__(self, direttore:Impiegato, dipartimento:Dipartimento):

            self._direttore = direttore
            self._dipartimento = dipartimento

        def setDirettore(self, direttore:Impiegato) -> None:
            self._direttore = direttore
            self.lista_direttori:dict[Impiegato, Dipartimento] = {}

            self.lista_direttori[0] = direttore

        def is_direttore(self, direttore:Impiegato) -> None:
            pass
            
        def getDirettore(self) -> Impiegato:
            return self._direttore
        
        def getDipartimento(self) -> Dipartimento:
            return self._dipartimento
        

            
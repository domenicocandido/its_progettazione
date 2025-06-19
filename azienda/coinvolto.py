from datetime import date
from typing import TYPE_CHECKING
class Coinvolto:from impiegato import Impiegato
from progetto import Progetto
from datetime import date

if TYPE_CHECKING:
    from impiegato import Impiegato
    from progetto import Progetto

class Coinvolto:

    @classmethod
    def add(cls, impiegato:Impiegato, progetto:Progetto) -> None:

        # crea il link l (impiegato, progetto)
        impiegato.add_link_coinvolto(l) #deve essere un metodo in impiegato che registra un link nell'impiegato
        progetto.add_link_coinvolto(l) #deve essere un metodo in progetto che registra un link nel progetto

    class _link:

        _impiegato:Impiegato
        _progetto:Progetto
        _data_inizio:date

        def __init__(self, impiegato:Impiegato, progetto:Progetto, data_inizio:date):

            self._impiegato = impiegato
            self._progetto = progetto
            self._data_inizio = data_inizio

        
        def get_impiegato(self) -> Impiegato:
            return self._impiegato
        
        def get_progetto(self) -> Progetto:
            return self._progetto
        
        def get_inizio(self) -> date:
            return self._data_inizio
        
        def is_coinvolto(self, impiegato: Impiegato, progetto:Progetto) -> bool:

            if impiegato in progetto:
                return True
            else:
                return False
from typing import Self

class RealGTZ(float):

    def __new__(cls, v: int | float | str | bool | Self) -> Self:

        n: float = super().__new__(cls, v)

        if n > 0:
            return n

        raise ValueError(f"Il numero inserito {v} è negativo o 0!")
    

class RealGEZ(float):

    def __new__(cls, v: int | float | str | bool | Self) -> Self:

        n: float = super().__new__(cls, v)

        if n >= 0:
            return n

        raise ValueError(f"Il numero inserito {v} è negativo!")
    
import re

class CodiceFiscale:
    def _init_(self, codice):
        if not self._valida_codice(codice):
            raise ValueError("Codice Fiscale non valido.")
        self.codice = codice.upper()

    def _str_(self):
        return self.codice

    def _eq_(self, other):
        if isinstance(other, CodiceFiscale):
            return self.codice == other.codice
        return False

    def _len_(self):
        return len(self.codice)

    @staticmethod
    def _valida_codice(codice):
        # Un codice fiscale valido è lungo 16 caratteri e segue un pattern specifico
        pattern = r"^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$"
        return bool(re.match(pattern, codice.upper()))

    def is_valid(self):
        return self._valida_codice(self.codice)

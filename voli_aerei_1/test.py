from volo import Volo
from compagnia import Compagnia
from aeroporto import Aeroporto
from custom_types import RealGTZ
from citta import Citta
from nazione import Nazione

nazione = Nazione("Francia")
città = Citta("Parigi", 2148000, nazione)

aeroporto_partenza = Aeroporto("CDG", "Charles de Gaulle")
aeroporto_arrivo = Aeroporto("ORY", "Orly")

compagnia = Compagnia("Air France", RealGTZ(1933))
compagnia.set_citta(città)

volo = Volo("AF456", RealGTZ(75), compagnia, aeroporto_partenza, aeroporto_arrivo)

print("Codice volo:", volo.get_codice())
print("Durata (minuti):", volo.get_durata_min())
print("Compagnia:", volo.get_compagnia().get_nome())
print("Città di origine della compagnia:", compagnia.get_citta().get_nome())
print("Partenza da:", volo.get_partenza().get_nome(), "-", volo.get_partenza().get_codice())
print("Arrivo a:", volo.get_arrivo().get_nome(), "-", volo.get_arrivo().get_codice())

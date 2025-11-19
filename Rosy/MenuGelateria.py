from MenuGelateria import MenuGelateria
from Antonia.classe_base import *

class MenuGelateria:
    def __init__(self):
        # Lista interna dei gusti disponibili nel menu
        self._gusti: list[Gusto] = []

    def aggiungi_gusto(self, gusto: Gusto) -> None:
        # Aggiunge un nuovo gusto al menu
        self._gusti.append(gusto)

    def rimuovi_gusto(self, nome: str) -> bool:
        """
        Rimuove un gusto dal menu dato il suo nome.
        Restituisce True se il gusto è stato rimosso, False se non trovato.
        """
        # Converto il nome in minuscolo per un confronto case-insensitive
        nome = nome.lower()

        # Ciclo tra tutti i gusti per trovare quello da rimuovere
        for gusto in self._gusti:
            if gusto.get_nome().lower() == nome:
                self._gusti.remove(gusto)
                return True  # Gusto trovato e rimosso
        return False  # Nessun gusto trovato con quel nome

    def lista_gusti(self) -> None:
        """
        Stampa la lista dei gusti presenti nel menu.
        Differenzia tra gusti normali, vegani e premium.
        """
        if not self._gusti:
            print("Il menu è vuoto")  # Nessun gusto disponibile
        else:
            print("\n=== Menu Gelateria ===")  # Intestazione del menu

            # Stampa ogni gusto in base al suo tipo
            for gusto in self._gusti:
                if isinstance(gusto, GustoPremium):
                    print(gusto.descrizione_premium())  # Descrizione per gusti premium
                elif isinstance(gusto, GustoVegano):
                    print(gusto.descrizione_vegano())   # Descrizione per gusti vegani
                else:
                    print(gusto.descrizione())         # Descrizione per gusti normali

#SOTTOCLASSI: 
# Sottoclasse: GustoPremium
class GustoPremium(Gusto):
    def __init__(self, nome, prezzo_base, allergeni=None, ingredienti_speciali=None, sovrapprezzo=0.0):
        super().__init__(nome, prezzo_base, allergeni)
        self.__ingredienti_speciali = ingredienti_speciali if ingredienti_speciali else []
        self.__sovrapprezzo = sovrapprezzo

    # Getter e setter
    def get_ingredienti_speciali(self):
        return self.__ingredienti_speciali

    def set_ingredienti_speciali(self, ingredienti):
        self.__ingredienti_speciali = ingredienti

    def get_sovrapprezzo(self):
        return self.__sovrapprezzo

    def set_sovrapprezzo(self, sovrapprezzo):
        self.__sovrapprezzo = sovrapprezzo

    # Metodo descrizione premium
    def descrizione_premium(self):
        base = super().descrizione()
        return f"{base}, Ingredienti speciali: {', '.join(self.__ingredienti_speciali)}, Sovrapprezzo: {self.__sovrapprezzo:.2f}€"


# Sottoclasse: GustoVegano
class GustoVegano(Gusto):
    def __init__(self, nome, prezzo_base, allergeni=None, base_vegetale="soia"):
        super().__init__(nome, prezzo_base, allergeni)
        self.__base_vegetale = base_vegetale

    # Getter e setter
    def get_base_vegetale(self):
        return self.__base_vegetale

    def set_base_vegetale(self, base):
        self.__base_vegetale = base

    # Metodo descrizione vegano
    def descrizione_vegano(self):
        base = super().descrizione()
        return f"{base}, Base vegetale: {self.__base_vegetale}"

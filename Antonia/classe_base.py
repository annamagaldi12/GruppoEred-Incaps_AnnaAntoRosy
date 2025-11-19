class Gusto:
    def _init_(self, nome: str, prezzo_base: float, allergeni: list):
        self.__nome = nome
        self.__prezzo_base = prezzo_base
        self.__allergeni = allergeni
        
    def get_nome(self):
        return self._nome
    def set_nome(self):
        return self.__nome
    
    # getter prezzo_base
    def get_prezzo_base(self):
        return self.__prezzo_base
    # setter prezzo_base
    def set_prezzo_base(self):
        return self.__prezzo_base
    # getter allergeni
    def get_allergeni(self):
        return self.__allergeni
    def set_allergeni(self):
        return self.__allergeni
    
    # metodo per descrizione del gusto
    def descrizione(self):
        return f"Gusto: {self._nome}, Prezzo base: {self.prezzo_base}€, Allergeni: {', '.join(self._allergeni)}"
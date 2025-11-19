
from MenuGelateria import MenuGelateria
from Antonia.classe_base import *

def menu_gelateria():
    menu = MenuGelateria()

    # Creazione iniziale gusti
    g1 = Gusto("Cioccolato", 1.50, ["latte"])
    g2 = Gusto("Vaniglia", 1.20, ["latte"])
    g3 = Gusto("Fragola", 1.30, [])

    gp1 = GustoPremium("Pistacchio", 1.80, ["latte"], ["pistacchi selezionati"], 0.50)
    gp2 = GustoPremium("Nocciola", 1.70, ["latte"], ["nocciole tostate"], 0.40)

    gv1 = GustoVegano("Mango", 1.60, [], "cocco")

    for g in [g1, g2, g3, gp1, gp2, gv1]:
        menu.aggiungi_gusto(g)

    while True:
        print("\n=== MENU PRINCIPALE GELATERIA ===")
        print("1. Mostra menu")
        print("2. Aggiungi gusto")
        print("3. Rimuovi gusto")
        print("4. Esci")
        scelta = input("Scegli un'opzione (1-4): ").strip()

        if scelta == "1":
            menu.lista_gusti()

        elif scelta == "2":
            tipo = input("Tipo di gusto (base/premium/vegano): ").strip().lower()
            nome = input("Nome del gusto: ").strip()
            prezzo = float(input("Prezzo base: ").strip())
            allergeni_input = input("Allergeni separati da virgola (vuoto se nessuno): ").strip()
            allergeni = [a.strip() for a in allergeni_input.split(",")] if allergeni_input else []

            if tipo == "base":
                g = Gusto(nome, prezzo, allergeni)
            elif tipo == "premium":
                ingredienti_input = input("Ingredienti speciali separati da virgola: ").strip()
                ingredienti = [i.strip() for i in ingredienti_input.split(",")] if ingredienti_input else []
                sovrapprezzo = float(input("Sovrapprezzo: ").strip())
                g = GustoPremium(nome, prezzo, allergeni, ingredienti, sovrapprezzo)
            elif tipo == "vegano":
                vegetale = input("Tipo vegetale: ").strip()
                g = GustoVegano(nome, prezzo, allergeni, vegetale)
            else:
                print("Tipo non valido.")
                continue

            menu.aggiungi_gusto(g)
            print(f"Gusto {nome} aggiunto al menu.")

        elif scelta == "3":
            nome = input("Nome del gusto da rimuovere: ").strip()
            if menu.rimuovi_gusto(nome):
                print(f"Gusto {nome} rimosso dal menu.")
            else:
                print("Gusto non trovato.")

        elif scelta == "4":
            print("Uscita dal programma.")
            break

        else:
            print("Opzione non valida. Riprova.") 
            
menu()
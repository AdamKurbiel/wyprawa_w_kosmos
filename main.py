#Stworzone przez Adam Kurbiel
from utils import ask_int

def setup_game():
    print("┌─ WYPRAWA W KOSMOS ─┐")
    print("│Autor:  Adam Kurbiel│")
    print("└────────────────────┘\n")

    expedition_name = input("> Wprowadź nazwę wyprawy: ")
    if not expedition_name:
        expedition_name = "Wielka wyprawa"

    spaceship_name = input("> Wprowadź nazwę statku kosmicznego: ")
    if not spaceship_name:
        spaceship_name = "Szybki statek"
    
    start_x = ask_int("> Pozycja startowa X (-80 do 80):",-80,80,0)
    start_y = ask_int("> Pozycja startowa Y (-80 do 80):",-80,80,0)

setup_game()
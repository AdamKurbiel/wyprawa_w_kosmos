#Stworzone przez Adam Kurbiel
from utils import ask_int, ask_choice
from world import World

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

    angle = ask_int("> Kąt startowy (0-359):",0,359,90)

    energy = ask_int("> Początkowa energia (50-250):",50,250,120)

    difficulty = ask_choice("Poziom trudności",['easy','normal','hard'])

    world_size = {
        "easy": 90,
        "normal":110,
        "hard":140
    }

    max_steps = {
        "easy":40,
        "normal":55,
        "hard":70
    }

    world = World(world_size[difficulty],difficulty)
    
    


setup_game()
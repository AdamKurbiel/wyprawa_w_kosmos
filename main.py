#Stworzone przez Adam Kurbiel
from utils import ask_int, ask_choice
from world import World
from entities import Spaceship

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
    spaceship = Spaceship(expedition_name,spaceship_name,start_x,start_y,angle,energy)

    return world, spaceship, max_steps[difficulty]
    
def show_intro(world,vehicle, max_steps):
    print(f"\n┌──Wyprawa: {vehicle.expedition_name}")
    print(f"├Pojazd: {vehicle.expedition_name}")
    print(f"├Pozycja startowa: ({vehicle.x},{vehicle.y})")
    print(f"├Kąt startowy: {vehicle.angle}")
    print(f"├Energia startowa: {vehicle.energy}")
    print(f"├Granice świata: {-world.size} do {world.size}")
    print(f"├Limit kroków: {max_steps}")
    print(f"└Cel misji: odnaleźć rdzeń energetyczny i przetrwać.")

def game_loop(world, vehicle, max_steps):
    history = []
    visited = []

    show_intro(world, vehicle,max_steps)

    while True:

        #Sprawdzanie czy gra się nie ma skończyć
        if vehicle.energy <= 0:
            reason = "Brak energii"
            status = "PORAŻKA"
            break
        
        if vehicle.integrity <= 0:
            reason = "Uszkodzenie pojazdu"
            status = "PORAŻKA"
            break

        if vehicle.steps >= max_steps:
            reason = "Przekroczono limit kroków"
            status = "(prawie) SUKCES"
            break
        
        if vehicle.found_core and world.distance_to_base(vehicle.x, vehicle.y) <= 10:
            reason = "Udany powrót z rdzeniem"
            status = "SUKCES"
            break


        print(f"KROK {vehicle.steps + 1}")
        print(f"Pozycja: ({vehicle.x},{vehicle.y})")
        print(f"Energia: {vehicle.energy}")
        print(f"Integralność: {vehicle.integrity}")
        print(f"Rdzeń znaleziony: {'TAK' if vehicle.found_core else 'NIE'}")

        


while True:
    world, vehicle, max_steps = setup_game()
    result = game_loop(world, vehicle, max_steps)

    again = input("\nUruchomić nową symulację? (t/n): ").lower()
    if again != "t":
        print("Do zobaczenia!")
        break
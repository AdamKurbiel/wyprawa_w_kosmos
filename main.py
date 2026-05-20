#Stworzone przez Adam Kurbiel
from utils import ask_int, ask_choice, separator
from world import World
from entities import Spaceship
from turtle_view import init_world, draw_step
from events import pick_event, announce_event
import random

def setup_game():
    #Podstawowa konfiguracja gry
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
    #Pokaż początkowe informacje
    print(f"\n┌──Wyprawa: {vehicle.expedition_name}")
    print(f"├Pojazd: {vehicle.name}")
    print(f"├Pozycja startowa: ({vehicle.x},{vehicle.y})")
    print(f"├Kąt startowy: {vehicle.angle}")
    print(f"├Energia startowa: {vehicle.energy}")
    print(f"├Granice świata: {-world.size} do {world.size}")
    print(f"├Limit kroków: {max_steps}")
    print(f"└Cel misji: odnaleźć rdzeń energetyczny i przetrwać.")

def choose_action():
    #wybór akcji
    print(separator(start=True))
    print("│DOSTĘPNE AKCJE:")
    print(separator())
    print("├1. Ruch naprzód")
    print("├2. Obrót w lewo")
    print("├3. Obrót w prawo")
    print("├4. Skanowanie terenu")
    print("├5. Tryb turbo")
    print(separator())
    return input("└> Wybór: ")
    

def game_loop(world, vehicle, max_steps):
    history = []
    visited = []
    event_log = []

    show_intro(world, vehicle,max_steps)
    init_world(world, vehicle)

    while True:
        #Sprawdzanie czy gra się nie ma skończyć
        if vehicle.energy <= 0:
            reason = "Brak energii"
            status = "PRZEGRANA"
            break
        
        if vehicle.integrity <= 0:
            reason = "Uszkodzenie pojazdu"
            status = "PRZEGRANA"
            break

        if vehicle.steps >= max_steps:
            reason = "Przekroczono limit kroków"
            status = "PRZEGRANA"
            break
        
        if vehicle.found_core:
            reason = "Udany powrót z rdzeniem"
            status = "SUKCES"
            break

        print(separator(start=True))
        print(f"│KROK {vehicle.steps + 1}")
        print(separator())
        print(f"├Pozycja: ({vehicle.x},{vehicle.y})")
        print(f"├Energia: {vehicle.energy}")
        print(f"├Integralność: {vehicle.integrity}")
        print(f"├Rdzeń znaleziony: {'TAK' if vehicle.found_core else 'NIE'}")
        print(separator(end=True))

        action = choose_action()
        print("\n=================" * 2)
        

        before_energy = vehicle.energy
        before_position = (vehicle.x, vehicle.y)

        #AKCJE
        match (action):
            case "1":
                log = vehicle.move(world)
            case "2":
                vehicle.turn(-45)
                log = "Statek obrócił się w lewo o 45 stopni."
            case "3":
                vehicle.turn(45)
                log = "Statek obrócił się w prawo o 45 stopni."
            case "4":
                log = world.scan_area(vehicle.x,vehicle.y)
                vehicle.energy -= 2
            case "5":
                log = vehicle.move(world,turbo=True)
            case _:
                log = "Niepoprawna akcja. Wykonuję automatyczny ruch."
                log += "\n│" + vehicle.move(world)
            
        world_result = world.apply_world_effect(vehicle)
        event_result = False

        event_chance = random.randint(0,9)
        
        if event_chance == 5:
            event_result = pick_event(vehicle, world)

        if world_result:
            visited.append(world_result)

        if event_result:
            event_log.append(event_result)
            

        print(separator(start=True))
        print("│RAPORT KROKU")
        print(separator())
        print(f"├{log}")

        if world_result:
            print(f"├{world_result}")

        if event_result:
            announce_event(event_result)
        
        print(f"├Pozycja przed ruchem: {before_position}")
        print(f"├Pozycja po ruchu: ({vehicle.x},{vehicle.y})")
        print(f"├Energia przed ruchem: {before_energy}")
        print(f"├Energia po ruchu: {vehicle.energy}")
        print(separator(end=True))

        history.append((vehicle.x, vehicle.y))
        draw_step(history)
        
        vehicle.steps += 1
    
    return {
        "status": status,
        "reason": reason,
        "history": history,
        "visited": visited
    }

def show_summary(vehicle, result):
    #finalne statystyki
    print(f"\n\n┌─{result['status'].upper()}")
    print(f"├Powód: {result['reason']}")
    print(f"├Nazwa wyprawy: {vehicle.expedition_name}")
    print(f"├Statek: {vehicle.name}")
    print(f"├Pozycja końcowa: ({vehicle.x},{vehicle.y})")
    print(f"├Liczba kroków: {vehicle.steps}")
    print(f"├Pozostała energia: {vehicle.energy}")
    print(f"├Integralność: {vehicle.integrity}")

    score = vehicle.calculate_score(result["status"])

    print(f"└WYNIK KOŃCOWY: {score} PUNKTÓW")

    if result['visited']:
        print("Najważniejsze zdarzenia:")

        unique_events = list(set(result["visited"]))

        for event in unique_events:
            print(f"- {event}")
        
    print()
    

    

while True:
    #pętla :)
    world, vehicle, max_steps = setup_game()
    result = game_loop(world, vehicle, max_steps)

    show_summary(vehicle,result)

    again = input("\nUruchomić nową symulację? (t/n): ").lower()
    if again != "t":
        print("Do zobaczenia!")
        break
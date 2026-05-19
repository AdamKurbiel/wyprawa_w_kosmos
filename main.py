#Stworzone przez Adam Kurbiel


def setup_game():
    print("┌─ WYPRAWA W KOSMOS ─┐")
    print("│Autor: Adam Kurbiel │")
    print("└────────────────────┘\n")

    expedition_name = input("> Wprowadź nazwę wyprawy: ")
    if not expedition_name:
        expedition_name = "Wielka wyprawa"

    spaceship_name = input("> Wprowadź nazwę statku kosmicznego: ")
    if not spaceship_name:
        spaceship_name = "Szybki statek"

setup_game()
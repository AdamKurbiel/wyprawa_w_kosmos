#walidacja liczb
SEPARATOR_LINE_LENGTH = 20

def separator(start = False, end = False):
    SEPARATOR_SIGN = "─"

    line = SEPARATOR_SIGN * SEPARATOR_LINE_LENGTH
    if end: return "└"+line
    return "├"+line if not start else "┌"+line

def ask_int(message, minimum, maximum, default):
    while True:
        value = input(message).strip()

        if value == "":
            return default

        try:
            number = int(value)

            if minimum <= number <= maximum:
                return number

            print(f"Podaj wartość od {minimum} do {maximum}.")

        except ValueError:
            print("Niepoprawna wartość.")

#walidacja wyborów
def ask_choice(message, choices):
    print(f"{message}: {', '.join(choices)}")

    while True:
        value = input("> Wybór: ").strip().lower()

        if value in choices:
            return value

        print("Niepoprawny wybór.")
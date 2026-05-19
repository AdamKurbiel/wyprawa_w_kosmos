#walidacja liczb
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
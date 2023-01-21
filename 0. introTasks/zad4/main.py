def kalkulator(num1: float, action: str, num2: float) -> float:
    action = action.lower()
    if action == "dodaj" or action == "add":
        return num1 + num2
    elif action == "odejmij" or action == "subtract":
        return num1 - num2
    elif action == "pomnoz" or action == "multiply":
        return num1 * num2
    elif action == "podziel" or action == "divide":
        return num1 / num2


liczby = [float(input("Podaj liczbe 1: ")), float(input("Podaj liczbe 2: "))]
dzialanie = str(input("Dzialanie: "))
print(kalkulator(liczby[0], dzialanie, liczby[1]))

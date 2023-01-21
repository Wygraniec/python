def greet(name: str, age: int):
    print("Cześć, jestem " + name + " i mam " + str(age), end=" ")

    if age == 1:
        print("rok")
    elif 12 <= wiek <= 14:
        print("lat")
    elif 2 <= age % 10 <= 4:
        print("lata")
    else:
        print("lat")


imie: str = input("Podaj imie: ")
wiek: int = int(input("Podaj wiek: "))
greet(imie, wiek)

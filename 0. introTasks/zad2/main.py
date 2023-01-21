def wzorek(size: int):
    for i in range(0, size + 1):
        for j in range(0, i):
            print("*", end=" ")
        print("")


n: int = int(input("Podaj rozmiar: "))
wzorek(n)

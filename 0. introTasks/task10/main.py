def christmasTree(maxSize: int):
    i: int = 1
    j: int = maxSize - 1
    while i <= maxSize + 1 and j >= 0:
        for m in range(0, int(j / 2)):
            print(" ", end="")
        for n in range(0, i):
            print("*", end="")
        j -= 2
        i += 2
        print()


rozmiar = int(input("Podaj rozmiar choinki: "))
christmasTree(rozmiar)

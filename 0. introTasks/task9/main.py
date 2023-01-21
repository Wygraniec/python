def sumList(arr) -> int:
    suma: int = 0
    for i in arr:
        suma += i
    return suma


size = int(input("Podaj ilosc liczb: "))
arr = []
for i in range(0, size):
    arr.append(int(input("Podaj liczbe " + str( i + 1) + ": ")))
print(sumList(arr))

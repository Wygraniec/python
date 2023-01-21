def isPrime(num: int) -> bool:
    if num < 0 or num == 1:
        return 0

    for i in range(2, num):
        if num % i == 0:
            return 0
    return 1


liczba = int(input("Podaj liczbe: "))

if isPrime(liczba):
    print("Liczba jest pierwsza")
else:
    print("Liczba nie jest pierwsza")
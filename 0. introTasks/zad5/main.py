def factorial(num: int) -> int:
    result: int = 1
    for i in range(num):
        result *= num
        num -= 1
    return result


liczba = int(input("Podaj liczbe: "))
print(factorial(liczba))

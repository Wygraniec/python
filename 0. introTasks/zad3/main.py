def power(base: float, exponent: int) -> float:
    result = base
    for i in range(1, exponent):
        result *= base
    return result


podstawa = float(input("Podaj podstawe potegi: "))
wykladnik = int(input("Podaj wykladnik potegi: "))
print(power(podstawa, wykladnik))

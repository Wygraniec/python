def bmi(height: float, weight: float) -> float:
    return weight / (height ** 2)


def stan(id: float) -> str:
    if id < 18.5:
        return "niedowaga"
    elif 18.5 <= id < 25:
        return "nadwaga"
    elif 25 <= id < 30:
        return "nadwaga"
    elif 30 <= id:
        return "otylosc"


wzrost = float(input("Podaj wzrost: "))
masa = float(input("Podaj mase: "))
print("BMI wynosi", end=" ")
print(bmi(wzrost, masa))
print(stan(bmi(wzrost, masa)))

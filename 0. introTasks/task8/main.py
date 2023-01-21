file = open("prawkaLata.txt", "r")
list = []
while True:
    line = file.readline()

    if not line:
        break

    linia = line.split(" ")
    linia.pop()
    linia[1] = int(linia[1])
    list.append(linia)

age = int(input("Podaj wiek: "))
print("Majac ", age, " lat mozna miec prawo jazdy kategori: ")
for i in range(0, len(list)):
    if age >= list[i][1]:
        print(list[i][0], end=", ")

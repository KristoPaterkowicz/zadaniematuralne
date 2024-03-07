plik = "liczby.txt"
dziel2 = 0
dziel8 = 0

with open(plik) as file:
    for linia in file:
        liczba = int(linia, 2)

        if liczba % 2 == 0:
            dziel2 += 1

        if liczba % 8 == 0:
            dziel8 += 1

print("Liczba liczb podzielnych przez 2:", dziel2)
print("Liczba liczb podzielnych przez 8:", dziel8)


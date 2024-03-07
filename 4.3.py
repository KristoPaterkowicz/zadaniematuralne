plik = "liczby.txt"

min = float("inf")
max = float("-inf")

wmin = 0
wmax = 0
w = 0

with open(plik) as file:
    for linia in file:
        liczba = int(linia, 2)
        w += 1

        if min > liczba:
            min = liczba
            wmin = w

        if max < liczba:
            max = liczba
            wmax = w

print("Wiersze: ", wmax, wmin)
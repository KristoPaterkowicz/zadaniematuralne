plik = 'liczby.txt'
count = 0
with open(plik) as file:
    for linia in file:
        zera = linia.count('0')
        jedynki = linia.count('1')
        if zera > jedynki:
            count += 1

print(f"Ilość liczb, które mają więcej zer niż jedynek: {count}")





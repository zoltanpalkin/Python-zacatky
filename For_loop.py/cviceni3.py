#Exercise 3: Calculate the sum of all numbers from 1 to a given number

seznam = []

cislo = int(input("Zadej cislo "))
soucet = sum(seznam)
for i in range(cislo+1):
    seznam.append(i)
    soucet = sum(seznam)
    print(seznam)
    print(soucet)


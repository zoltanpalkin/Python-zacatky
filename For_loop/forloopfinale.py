#1) vypiš čísla od 1 do 100 pomocí for loopu , 
#2) místo každého sudého čísla se vypíše fizz , 
#3) místo každého čísla násobku 5(5,10,15...) se vypíše fuzz , 
#4) místo každého čísla ktery je sudy a nasobek nebo delitelnz 5 se vypíše fizzfuzz
#5) Dat vsechny cislo ktery nejsou ani fizz ani fuzz ani fizz fuzz do seznamu


seznam = []
pocet_Fizzu = 0
pocet_Fuzzu = 0
pocet_FizzFuzzu = 0

for j in range(1, 101):
    if j % 2 == 0 and j % 5 == 0:
        print("FizzFuzz")
        pocet_FizzFuzzu += 1
    elif j % 2 == 0:
        print("Fizz")
        pocet_Fizzu += 1
    elif j % 5 == 0:
        print("Fuzz")
        pocet_Fuzzu += 1
    else:
        seznam.append(j)
        print(j)

print(f"Pocet Fizzu: {pocet_Fizzu}")
print(f"Pocet Fuzzu: {pocet_Fuzzu}")
print(f"Pocet FizzFuzzu: {pocet_FizzFuzzu}")
print(f"Seznam zbyvajicich cisel: {seznam}")





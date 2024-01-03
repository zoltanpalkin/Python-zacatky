#Napište program, který projde kolekci čísel a nalezne mezi nimi největší a nejmenší číslo. Nepoužívejte funkce min a max!
import random 

seznam_cisel = []

for _ in range(10):
    nahodne_cisla = random.randrange(0,100)
    seznam_cisel.append(nahodne_cisla)
seznam_cisel.sort()

print(f" nejmensi cislo v seznamu {seznam_cisel[0]}")
print(f" nejvetsi cislo v seznamu {seznam_cisel[-1]}")
print(seznam_cisel)

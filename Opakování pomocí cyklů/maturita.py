#Napište program, který v kolekci obsahuje seznam maturitních otázek. Poté se spustí cyklus, 
#který se opakuje do té doby, dokavaď v seznamu nějaká otázka zbývá. Kdykoliv uživatel zmáčkně klávesu ENTER, tak program jednu z otázek náhodně vylosuje a 
#ypíše na obrazovku. Otázky budou voleny náhodně. Podívejte se do modulu random, jaké by funkce by se vám mohly hodit pro tento účel.

import random
import keyboard
from keyboard import press
maturitni_otaza = [1,2,3,4,5]
cyklus = False
while not cyklus:
    volba = input("Vylosujte nahodnu otazku")
    if volba == '':
        nahodna = random.choice(maturitni_otaza)
        print(nahodna)
        maturitni_otaza.remove(nahodna)
        if maturitni_otaza == []:
            print("Nejsou jiz zadne otazky")
            cyklus = True





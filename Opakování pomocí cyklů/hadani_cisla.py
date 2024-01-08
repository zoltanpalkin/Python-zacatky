#Napište program, kde uživatel hádá náhodné číslo v rozmezí od 1 do nějaké maximální meze. 

#Na začátku je maximální mez nastavena na hodnotu 2. S každým uhádnutým číslem se mez zvětšuje o jedna, 
#takže pokud uživatel v prvním kole číslo uhádne, tak v příštím kole již hádá mezi 1 a 3. Pokud uživatel číslo neuhádně, 
#tak hádáná hodnota musí zůstat stejná a uživatel jen dostane nápovědu, jestli musí hádat číslo nižší nebo vyšší. Uživatel má 3 životy, 
#které pokud dojdou, tak hra končí. Po ukončení hry se na obrazovku vypíše nějakým vhodným způsobem vypočítané skóre.


import random
MAXIMALNI_MEZ = 2

seznam_cisel = range(1,MAXIMALNI_MEZ)

NAHODNE_CISLO = random.randint(1,MAXIMALNI_MEZ) 

POCET_ZIVOTU = 3

SKORE = 0

while POCET_ZIVOTU > 0 :
    hadani = int(input("Uhadnete cislo"))
    
    if hadani == NAHODNE_CISLO:
        print("uhadli jste cislo")
        SKORE +=1
        MAXIMALNI_MEZ +=1
        print(MAXIMALNI_MEZ)
    
   
    elif hadani != NAHODNE_CISLO and hadani > NAHODNE_CISLO:
        print("je to mensi cislo")
        POCET_ZIVOTU -=1
    
    elif hadani != NAHODNE_CISLO and hadani < NAHODNE_CISLO:
        print("je to vetsi cislo")
        POCET_ZIVOTU -=1
    
    if POCET_ZIVOTU == 0:
        print(f"Tve skore {SKORE}")
        print("jste prohrali")
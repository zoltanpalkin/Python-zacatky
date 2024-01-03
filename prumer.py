#Napište program, který bude žádat uživatele o zadávání číselných dat z 
# klávesnice do té doby, dokavaď nenapíše řetězec STOP. 
#Poté vypíše na obrazovku aritmetický průměr z hodnot. 
#Přidávání do kolekce se provádí příkazem append. Na začátku si budete muset vytvořit prázdnou kolekci.

konec = False
seznam = []
while not konec:
    cisla = input("Zadavejte Cislo pokud program nerekne stop")
    if cisla == 'STOP':
        print(prumer)
        konec = True
    else:
        cislo = int(cisla)
        seznam.append(cislo)
        soucet = sum(seznam)
        delka = len(seznam)
        print(seznam)
        prumer =  soucet / delka


    

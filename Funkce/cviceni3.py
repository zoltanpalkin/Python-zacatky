#Exercise 3: Return multiple values from a function

cislo1 = 10
cislo2 = 20

def pocitani(cislo1,cislo2):
    soucet =  cislo1+cislo2
    odecet = cislo2-cislo1
    print(soucet,odecet)
pocitani(cislo1,cislo2)

def pocitani(cislo1,cislo2):
    soucet =  cislo1+cislo2
    odecet = cislo2-cislo1
    return soucet,odecet
vysledek = pocitani(cislo1,cislo2)
print(vysledek)
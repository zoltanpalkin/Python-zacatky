#navrhnete kalkulacku která umí + - * / % domocnina na 2



def scitani():
    scitani = sum(seznam)
    return scitani




x = False


seznam = []

while x is not True:
    
    cislo = input(f"zadejte cislo") 
    cislo1 = input("zadejte 2 cislo ")
    operato = input("Zadejte operanta")

    seznam.append(cislo,cislo1)
    
    if operato == '+':  
        print("zvolil jste scitani")
        print(scitani())
    elif operato == 'skip':
        continue
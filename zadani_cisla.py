#Napište program, který neskončí dokavaď nezadáá uživatel 
#ze standardního vstupu číslo, které po přetypování nevyhodí chybu.
while True:
    try:
        cislo = input("Zadej cislo ")   
        if  cislo == int:
            float(cislo)
        
        print(f"prevedeno na int{cislo}")

    except ValueError:
        print("chyba toto neni cislo")
#Implement a function to calculate the factorial of a given number.

fakt = int(input("Zadejte cislo, pro které chcete faktorial: "))
nasobek = 100000

def vypocet(fakt):
    faktorial = 1
    for i in range(1, fakt + 1):
        faktorial *= i
    return faktorial

vysledek = vypocet(fakt)
print(f"Faktorial z {fakt} je {vysledek}")



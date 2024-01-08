#Realizujte algoritmus přihlašování do SIM karty. 
#Program vás požadá o zadání správného PINu SIM karty. Na zadání máte 3 pokusy. Pokud se trefíte do správného PINu, 
#pak vám aplikace vypíše informaci o úspěšném přihlášení do SIM karty. Pokud se netrefíte, pak vás požadá o korektní zadaní. 
#Pokud se netrefíte 3x, tak aplikace vypíše informaci o zablokování SIM karty.

print("VODAFONE")

sim1 = 1234
zacatek = 3
while zacatek > 0:

        prihlasovani = int(input("Zadejte spravny pin SIM karty"))

        if prihlasovani == sim1:
            print("Jste se prihlasily" )
            break
        elif prihlasovani != sim1:
            print("neprihlasilz jste se")
            zacatek -= 1
            print(f"mate jeste {zacatek} pokusu")
            continue
if zacatek == 0:
            print("mate BKLOK ")
    

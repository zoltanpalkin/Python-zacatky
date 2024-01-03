#Vytvořte seznam ntic, který naplňte dvojicemi (jméno, počet samohlásek ve jméně). Jména jsou zadaná v předpřipraveném seznamu. Použijte k tomu metodu count.

jmena = ["Pavel", "Milan", "Alena", "Vladimir"]
samohlaski = ('a', 'e', 'i', 'o', 'u')

for jmeno in jmena:
    pocet = 0  # Reset the count for each name
    for pismeno in jmeno:
        if pismeno.lower() in samohlaski:
            pocet += 1  # Increment the count for each vowel

    finale = (pocet, jmeno)
    print(finale)




            

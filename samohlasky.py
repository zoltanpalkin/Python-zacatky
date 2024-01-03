#Napište program, který projde slovo a spočítá v něm počet samohlášek.

seznam_samohlasek = ['a','e','i','o','u']

slovo = input("Zadejte slovo")
for pismeno in seznam_samohlasek:
    if pismeno in slovo:
        
        pocet = slovo.count(pismeno)
        print(pocet)

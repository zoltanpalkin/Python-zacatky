#Naprogramujte konzolovou verzi hry šibenice. Hra má skryté slovo, 
#které uživatel nevidí. Místo něj vidí na obrazovku na počátku pouze podtržítka. 
#Hra ho požádá o zápis písmenka. Pokud dané písmenko už v minulosti hádal, tak ho hra požádá o hádání znova. 
#Pokud ho nehádal, tak hra program zjistí, zda se někde zadané písmenko nachází v odkryté tajence. Pokud ne, 
#tak se hráčovi ubere život. Pokud ano, tak bude místo podtržítka písmenko odkryto. Hra končí v případě uhádnutí celého slova nebo když hráčovi dojdou životy.

seznam = ["slovo"]




print("SIBENICE")

# pocet_zivotu = 7

# while pocet_zivotu != 0:

#     hadani = input("Hadejte slova")

#     for slova in seznam:
#        for pismena in slova:
#             print(f"{pismena}")
pocet_zivotu = 7
seznam = ["python", "java", "ruby"]  # Add your own words to the list

for slovo in seznam:
    hadani = "_" * len(slovo)  # Initialize with underscores for each letter in the word

    while pocet_zivotu > 0 and "_" in hadani:
        print(f"Current state: {hadani}")
        hadane_pismeno = input("Guess a letter: ")

        if hadane_pismeno in slovo:
            print("Correct!")
            # Update the guessed word with the correctly guessed letter
            hadani = "".join([p if p == hadane_pismeno or hadani[i] != "_" else "_" for i, p in enumerate(slovo)])
        else:
            pocet_zivotu -= 1
            print(f"Incorrect! Lives left: {pocet_zivotu}")

    if "_" not in hadani:
        print(f"Congratulations! You guessed the word: {slovo}")
    else:
        print(f"Out of lives. The correct word was: {slovo}")

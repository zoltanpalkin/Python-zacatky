#Naprogramujte konzolovou verzi hry šibenice. Hra má skryté slovo, 
#které uživatel nevidí. Místo něj vidí na obrazovku na počátku pouze podtržítka. 
#Hra ho požádá o zápis písmenka. Pokud dané písmenko už v minulosti hádal, tak ho hra požádá o hádání znova. 
#Pokud ho nehádal, tak hra program zjistí, zda se někde zadané písmenko nachází v odkryté tajence. Pokud ne, 
#tak se hráčovi ubere život. Pokud ano, tak bude místo podtržítka písmenko odkryto. Hra končí v případě uhádnutí celého slova nebo když hráčovi dojdou životy.

import random
seznam = ['magazin','polevka','mama']
zivoty = 8
while zivoty > 0:
    print("SIBENICE")

    nahodne_slovo = random.choice(seznam)

    skryte_slovo = nahodne_slovo[:]
    skryte_slovo[1] = "_______"

    hadani = input("Hadate skryte slovo :D")
    
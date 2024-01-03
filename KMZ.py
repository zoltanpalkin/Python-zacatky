#Upravte váš kód na 
#kámen-nůžky-papír z předchozího cvičení na verzi hry, 
#ve které vyhrává hráč nebo počítač až po dvou vítězných kolech.


import time
import random
import threading
from playsound import playsound
#INTRO
# Songa

def playIntro():
    playsound('C:\\Users\\PC2022-ZOLTAN\\SONgy\\SONGA.mp3', True)

# Start playing the intro sound in a separate thread
play_thread = threading.Thread(target=playIntro)
play_thread.start()


intro = 2
while intro > 0:
        print("KAMEN")
        intro -1
        time.sleep(2)
            
        print("NUZKY")
        intro -1
        time.sleep(2)
   
        print("PAPIR")
        time.sleep(2)

        print("TED")
        time.sleep(2)

        print("TVURCE")
        time.sleep(2)

        print("Hudba")
        time.sleep(2)

        print("Zoltan")
        time.sleep(2)

        print("Backend programming")
        time.sleep(3)
        print("Zoltan")
        time.sleep(3)
        print("GLHF")
        time.sleep(3)
        stop_music_flag = False
        break
play_thread.join()

kola = 2
vyhra = 0
prohra = 2
while kola > 0:
    hrac = input("KAMEN NUZKY PAPIR TED ZACINAAAAA")
    volby = ["kamen", "nuzky", "papir"]
    protivnik = random.choice(volby)
    if hrac == volby[0] and protivnik == volby[2] and kola ==2 or 1 :
        print(f"jste prohrali, protivnik mel {protivnik}")
        kola -=1
        prohra -=1
        playsound('C:\\Users\\PC2022-ZOLTAN\\SONgy\\prohral.mp3')
        print(f"mate jeste jeno kolo{kola}")
    elif hrac == volby[0] and protivnik == volby[1]  and kola ==2 or 1:
        print(f"jste vyhrali protivnik mel {protivnik}")
        kola -=1
        vyhra +=1
    elif hrac == volby[1] and protivnik == volby[2] and kola ==2 or 1:
        print(f"jste vyhrali protivnik mel {protivnik}")
        kola -=1
        vyhra +=1
        print(f"mate jeste jeno kolo{kola}")
    elif hrac == volby[1] and protivnik == volby[0] and kola ==2 or 1:
        print(f"jste prohrali, protivnik mel {protivnik}")
        playsound('C:\\Users\\PC2022-ZOLTAN\\SONgy\\prohral.mp3')
        kola -=1
        prohra -=1
        print(f"mate jeste jeno kolo{kola}")
    elif hrac == volby[2] and protivnik == volby[0] and kola ==2 or 1:
        print(f"jste vyhrali, protivnik mel {protivnik}")
        kola -=1
        vyhra +=1
        print(f"mate jeste jeno kolo{kola}")
    elif hrac == volby[2] and protivnik == volby[1] and kola !=2:
        print(f"jste prohrali, protivnik mel {protivnik}")
        playsound('C:\\Users\\PC2022-ZOLTAN\\SONgy\\prohral.mp3')
        kola -=1
        prohra -=1
        print(f"mate jeste jeno kolo{kola}")
    elif hrac == volby and protivnik == volby :
        print("remiza")
        kola +=0
        print(f"mate jeste {kola} kola")
        playsound('C:\\Users\\PC2022-ZOLTAN\\SONgy\\SONGA.mp3')
    elif kola == 0 and vyhra == 2 and prohra ==0:
        break
if vyhra == 2:
    print("JSTE VYHRAL")
    playsound('C:\\Users\\PC2022-ZOLTAN\\SONgy\\lol.mp3')
elif prohra == 0:
    print("jste prohral")
    playsound('C:\\Users\\PC2022-ZOLTAN\\SONgy\\loln.mp3')



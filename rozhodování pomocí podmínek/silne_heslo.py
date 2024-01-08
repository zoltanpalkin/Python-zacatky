#Napište program, který zjistí, zda zadané heslo uživatelem 
#je silné. heslo musí mít alespoň jedno 
#velké písmeno, jedno malé písmeno, jednu 
#číslici, jeden speciální znak a minimální délka musí být alespoň 8 znaků.

import string
while True:
    heslo = input("Zadejte heslo")
    lower = list(string.ascii_lowercase)  
    upper = list(string.ascii_uppercase)
    if len(heslo) < 8:
        print("musite mit alespon 8 znaku")
        continue
    elif not any(char in lower for char in heslo) and not any(char in upper for char in heslo):
        print("musite mit alespon 1 male a jedno velke pimeno")
        continue
    elif not any(char in string.punctuation for char in heslo):
        print("Musite mit alespon jedno 1 specialni znak")
        continue
    elif not any(char.isdigit() for char in heslo):
        print("musite mit alespon jednu cislici")
        continue
    else:
        print(f"Mate silne heslo {heslo}")
        break
    
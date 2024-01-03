palindrom = input("Zadejte slovo, zda je plaindrom")
obr = palindrom[::-1]
if obr == palindrom:
    print("JE TO PLAINDROM BRACHO")
    print(f"vis proc, porotze slovo {obr} je stejny jak {palindrom}")
else:
    print(f"NENI TO PLAINDROMBRACHO, protoze {palindrom} neni stejny jak {obr} kokotko")
#Napište kód, který požádá uživatele o login a heslo. P
#rogram následně zkontroluje, zda se zadaná dvojice (login, heslo) nachází v seznamu registrovaných uživatelů. 
#Pokud ne, tak program zjistí, zda se nachází alespoň login v seznamu registrovaných. Pokud tam login nalezne, tak vypíše hlášku o nesprávném hesle. 
#Pokud se tam nenachází ani login, tak program dovolít uživateli se registrovat - přidá se zadaný login a heslo mezi registrované uživatele.


logins = [('pepa','123'),('Hana','888'),('jana','777')]

login = input("Zadejte login")
heslo = input("zadejte heslo")

for jmeno,pasword in logins:
    if (login, heslo) in logins:
        print(f"jste prihlaseny{login}")
    
    elif login in logins and heslo != logins :
        print("mate spatne heslo")
    elif login != logins and heslo in logins:
        print("spatnz login")

    elif login != logins and heslo != logins:
        otazka = input("nemate spravne login prejete si zaregistrovat<")
        if otazka == 'ANO':
            novy_login = input("Zadejte novy ;login")
            novy_heslo = input("zadejte nove heslo")
    
            logins.append((novy_login, novy_heslo))
            print(logins)
        if login == 'NE':
            print("nekdy priste")

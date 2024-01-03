#Napište program, který pomocí for cyklu proiteruje řídící proměnnou od hodnoty 0 do hodnoty 100. Pokud číslo v řídící proměnné bude liché, pak bude číslo uloženo 
#do kolekce lichá_čisla. Pokud bude sudé, 
#tak do kolekce sudá_čísla. Sudost nebo lichost můžete zjistit pomocí operace modulo (značí se procentem v jazyce python).

cisla = range(0,100)
suda_cisla = []
licha_cisla = []
cisla_3 = []
for seznam_cisle in cisla:
    if seznam_cisle%2 == 0:
        suda_cisla.append(seznam_cisle)
    elif seznam_cisle%1 == 0:
        licha_cisla.append(seznam_cisle)
    if seznam_cisle%3 ==0:
        cisla_3.append(seznam_cisle)
print(cisla_3)
print(f"{licha_cisla}")
print(f"{suda_cisla}")


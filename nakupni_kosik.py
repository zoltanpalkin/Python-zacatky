#Napište program, do kterého uživatel 
#napíše název produktu a množství, které chce zakoupit daného produktu. 
#Až uživatel napíše ZAPLATIT, tak program ukončí zadávání zboží do košíku a vypíše na obrazovku celkovou cenu za nákup.



produkty = [
  ("banan", 10),
  ("rohlik", 3),
  ("pastika", 30),
  ("hermelin", 50),
  ("chleba", 30),
  ("salam", 60),
  ("kecup", 70),
  ("eidam", 40),
  ("mandarinka", 8),
  ("okurka", 10),
]
kosik = [ ]
produkty1= produkty.copy()
while True:
    zbozi = input("Prosim zadejte zbozi")
    mnozstvi = int(input("prosim zadejte mnozstvi"))
    if zbozi == 'ZAPLATIT':
        break
    for nakoupit in produkty1:
      if zbozi == nakoupit[0]:
          kosik.append((zbozi,mnozstvi * nakoupit[1]))
          print(kosik)
for uctenka in kosik:
  print(f"{uctenka[0]},{uctenka[1]}")
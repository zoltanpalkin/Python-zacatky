#Exercise 14: Reverse a given integer number
cislo = 76542
obracene_cislo = 0
while cislo > 0:
    reminder = cislo % 10
    obracene_cislo = (obracene_cislo * 10) + reminder
    cislo = cislo // 10
print(obracene_cislo)
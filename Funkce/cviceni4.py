#Exercise 4: Create a function with a default argument

def informace(jmeno,vek = "30",plat = "9000"):
    print(f"Podrobne informace{jmeno,vek,plat}")

informace('Janek','70','300')
informace('Vojta',)
#Mějme seznam hráčů a jejich nahrané skóre ve hře:

hraci = [("Pavel", 5), ("Honza", 3), ("Jana", 7), ("Milan", 4), ("Michaela", 9)]
hraci_seznam = [] 
for skore in hraci:
    hraci_seznam.append(skore)
    hraci_seznam = sorted(hraci, key=lambda x: x[1])

print(hraci_seznam)
print(hraci_seznam[0])
print(hraci_seznam[4])
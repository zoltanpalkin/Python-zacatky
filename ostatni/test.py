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

produkty1 = produkty.copy()  # Create a copy of the original list

kosik = []  # Initialize the shopping cart before the loop

for nakoupit in produkty1:
    zbozi = input("Dobry den, co si prejete nakoupit: ")
    mnozstvi = int(input("Kolik toho bude: "))

    if zbozi == nakoupit[0]:
        kosik.append((zbozi, mnozstvi, mnozstvi * nakoupit[1]))
        print(f"Uspesne jsme to pridali do kosiku: {kosik}")

# Display the final shopping cart
print("Vas nakupni kosik obsahuje:")
for item in kosik:
    print(f"{item[0]} - mnozstvi: {item[1]}, cena: {item[2]}")

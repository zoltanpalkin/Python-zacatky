#Exercise 5: Create an inner function to calculate the addition in the following way


def prijem_hodnot(hodnota_a,hodnota_b):
    a = hodnota_a**2
    def vypocet_hodnot(hodnota_a,hodnota_b):
        return hodnota_a+hodnota_b
    
    plus = vypocet_hodnot(hodnota_a,hodnota_b)
    return plus+5

hotovo = prijem_hodnot(5,10)
print(hotovo)


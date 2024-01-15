#Write a function that takes a number as an argument and returns its square.

kvadr  = int(input("Zadejte cislo a ono vam to vrati v square"))

def square(kvadr):
    soucet = kvadr*kvadr
    return soucet
x = square(kvadr)
print(f"kvadr je {x}")
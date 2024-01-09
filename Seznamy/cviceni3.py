#Exercise 3: Turn every item of a list into its square

seznam = [1, 2, 3, 4, 5, 6, 7]
novy_seznam = []
for j in seznam:
    kraceni =j **2
    print(kraceni)
    novy_seznam.append(kraceni)
print(novy_seznam)
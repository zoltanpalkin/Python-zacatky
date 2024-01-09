#Exercise 7: Check if a value exists in a dictionary

sample_dict = {'a': 100, 'b': 200, 'c': 300}
hledana_hodnota = 200
x = sample_dict.values()
if hledana_hodnota in x:
    print(f"je tu 200")
    print(x)
else:
    print("neni")
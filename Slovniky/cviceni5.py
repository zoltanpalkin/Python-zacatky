#Exercise 5: Create a dictionary by extracting the keys from a given dictionary
# Keys to extract
keys = ["name", "salary"]
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
    
    }

for j in keys:
 newDict = {j: sample_dict[j]}
 print(newDict)


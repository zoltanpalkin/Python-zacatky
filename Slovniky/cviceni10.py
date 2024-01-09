#Exercise 10: Change value of a key in a nested dictionary
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
x = sample_dict.values()
print(f"brad nema penize{x}")


sample_dict['emp3']['salary'] = 8000
print(f"Brad dostal penize {sample_dict}")
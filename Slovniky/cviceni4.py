#Exercise 4: Initialize dictionary with default values

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

slovnik = dict.fromkeys(employees,defaults)
print(slovnik)
#Exercise 15: Use a loop to display elements from a given list present at odd index positions
seznam = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for j in seznam[1::2]:
    if j % 2 == 0:
        print(j)
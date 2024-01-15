seznam = []

konec = False
done = False

# ADD to-do list
while not konec:
    delat = input("Zadejte dnesni program: ")
    
    seznam.append(delat)
    
    if delat.lower() == 'konec':
        konec = True

print(f"Dneska mate na delanou: {seznam}")

# Mark tasks as done
while not done:
    mark = input("Prejete si neco oznacit jako hotovo? (Zadejte task nebo 'konec' pro ukonceni): ")
    
    if mark.lower() == 'konec':
        done = True
    elif mark in seznam:
        index = seznam.index(mark)
        seznam[index] += " - DONE"

print(f"Vase upraveny seznam: {seznam}")

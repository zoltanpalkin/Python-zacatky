# Add Task:

#1 Write a function that allows the user to add tasks to the to-do list.
#HOTOBO


#View Tasks:

# Create a function to display all the tasks in the to-do list.
# Mark Task as Done:

# Implement a function to mark a task as done or completed.
# Delete Task:

# Write a function to remove a task from the to-do list.
# Save to File:

# Implement a function to save the to-do list to a file, so the tasks persist between program runs.
# Load from File:

# Create a function to load tasks from a file when the program starts.
# User Interface:

# Develop a simple user interface that allows users to interact with the to-do list manager. Use a menu system to navigate through options.
# Date and Time Stamps:

# Add the ability to include date and time stamps for each task (when it was added or completed).
# Task Prioritization:

# Extend the program to allow users to set priorities for tasks (e.g., high, medium, low).
# Task Filtering:

# Implement a function to filter tasks based on their status (done or not done), priority, or date.

seznam = []

konec = False
done = False
hotv = False
#ADDD to do list
while not konec:
    delat = input("Zadejte dnesni program")

    seznam.append(delat)
    if delat == 'konec':
        konec = True
print(f"dneska mate na delanou{seznam}")
while not done:
    mark = input("Prejete si neco oznacit jako hotovo? (Zadejte task nebo 'konec' pro ukonceni): ")
    
    if mark.lower() == 'konec':
        done = True
    elif mark in seznam:
        index = seznam.index(mark)
        seznam[index] += " - HOTOVO"
print(f"vas upraveny{seznam}")
while not hotv:
    odstranuit = input("Prejete si neco odstraniut(Zadejte task nebo 'konec' pro ukonceni): ")
    
    if odstranuit.lower() == 'konec':
        hotv = True
    elif odstranuit in seznam:
        seznam.remove(odstranuit)
print(f"vas upraveni {seznam}")




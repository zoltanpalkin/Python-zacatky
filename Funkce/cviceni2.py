#Exercise 2: Create a function with variable length of arguments
# call function with 3 and  2 arguments




def cisla(*args):
    for arg in args: 
        print(arg)
cisla(1,2,3,4,5,5)
cisla(1,23,4)
#Exercise 6: Create a recursive function

def rekurziva(hodnota):
    if hodnota:
        return hodnota + rekurziva(hodnota - 1)
    else:
        return 0
hotovo = rekurziva(10)
print(hotovo)

# def addition(num):
#     if num:
#         # call same function by reducing number by 1
#         return num + addition(num - 1)
#     else:
#         return 0

# res = addition(10)
# print(res)
#Exercise 6: Count the total number of digits in a number

cislo = 75869
pocet = 0
while pocet != 0:
    # floor division
    # to reduce the last digit from number
    cislo = cislo // 10

    # increment counter by 1
    cislo = cislo + 1
print("Total digits are:", cislo)
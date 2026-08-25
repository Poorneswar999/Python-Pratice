'''
A bakery needs to track its flour stock after a day of baking. Write a program that takes the initial stock, flour used for bread, and flour used for cakes as input. Calculate the remaining stock and determine if it is strictly less than 50 units. Input Format: Three integers on separate lines representing initial stock, bread usage, and cake usage. Output Format: The remaining stock on the first line and the boolean result (True or False) on the second line.
'''
inStock = int(input())
forBread = int(input())
forCake = int(input())
finalValue = inStock - forBread - forCake
print(finalValue)
print(finalValue<50)

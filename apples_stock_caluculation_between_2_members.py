'''
A farmer has several baskets, each containing the same number of apples. Calculate the total number of apples and the remainder left after dividing the total equally among 3 friends. Finally, check if the total number of apples is strictly greater than 50. Input Format: Two integers on separate lines representing the number of baskets and apples per basket. Output Format: Three lines containing the total count, the remainder, and the comparison result (True/False).
'''
noBasket = int(input())
applePer = int(input())
total = noBasket*applePer
print("Total apples:",total)
print("Number of Apples per Person:",total%3)
print("Is stock more than 50: ",total>50)

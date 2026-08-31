'''
A warehouse tracker needs to calculate the total value of inventory for a specific item. Write a program that reads the item's name, the quantity in stock, and its unit price from the input. Calculate the total value by multiplying the quantity by the price and display the item name and total value. 
Input Format: Line 1: Item Name (String). Line 2: Quantity (Integer). Line 3: Unit Price (Float). 
Output Format: Two lines; the first line showing 'Item: ' followed by the name, and the second line showing 'Total: ' followed by the calculated value.
'''

product = input("Enter the Prodect Name : ")
quantity = int(input("Enter the Quantity : "))
price = float(input("Enter the Price : "))

print("Item:",product)
print("Total:", quantity * price)

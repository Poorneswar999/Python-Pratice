'''
Electricity Billing System Based on Unit Range with Subsidy and Surcharge
Problem Statement
An electricity department charges customers based on the following slabs:
Units Rate per Unit
0-100 ₹1.5
101-200 ₹2.5
201-500 ₹4
Above 500 ₹6
Additionally:
• If the customer is a senior citizen, a 10% subsidy is applied.
• If total units exceed 800, a surcharge of 5% is applied.
Write a Python program to calculate the final bill amount.

Input Format
units
is_senior_citizen
Output Format
Final Bill Amount
Constraints
0 <= units <= 5000
is_senior_citizen = True / False

Test Case 1
Input
250
True
Output
900

Test Case 2
Input
900
False
Output
5670
'''
units = int(input("Enter the no of units: "))
isSenior = input("Is you a senior citizen(True / False): ")
totalAmount = 0
if units <= 100:
    totalAmount = units * 1.5
elif units <= 200:
    totalAmount = units * 2.5
elif units <= 500:
    totalAmount = units * 4
else :
    totalAmount = units * 6


if isSenior=="True":
    totalAmount -= totalAmount * 0.1

if units > 800:
        totalAmount += totalAmount * 0.05

print("Total Amount is",int(totalAmount))

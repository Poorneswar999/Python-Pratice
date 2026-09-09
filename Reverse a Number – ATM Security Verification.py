'''
Reverse a Number – ATM Security Verification 
An ATM security system sometimes needs to process numbers in reverse order for verification purposes. 
For example, if a transaction reference number is 12345, the system should be able to generate 54321. 
You are asked to create a simple program that reverses a number without converting it into a string. 
Problem Statement Write a Python program to reverse a given integer using a loop. 
Requirements 
• Take an integer as input.  
• Use mathematical operations and a loop.  
• Do not convert the number into a string.  
• Display the reversed number.  
Example Input: 
Enter a number: 12345 
Output: Reversed Number: 54321 
Test Cases 
Input    Expected Output
12345     54321
9876      6789
1000       1
505       505
123       321 
'''
n = int(input("Enter the pin: "))
re = 0
for i in range(len(str(n))):
  r = n%10
  re = (re*10) + r
  n = n//10
print(re)

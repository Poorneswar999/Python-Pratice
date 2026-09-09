'''
A school teacher wants to create a small Python program to help students practice multiplication tables. 
Instead of manually writing the table every time, the teacher wants a program where a student 
enters any number and the program automatically generates its multiplication table from 1 to 10. 
Problem Statement Write a Python program that accepts a number from the user and prints its multiplication table from 1 to 10. 
Requirements 
• Take one integer as input.  
• Use a loop to generate the table.  
• Print the result in the format:  
5 x 1 = 5 
5 x 2 = 10 
... 
5 x 10 = 50 
Example Input: 
Enter a number: 7 
Output: 
7 x 1 = 7 
7 x 2 = 14 
7 x 3 = 21 
7 x 4 = 28 
7 x 5 = 35 
7 x 6 = 42 
7 x 7 = 49 
7 x 8 = 56 
7 x 9 = 63 
7 x 10 = 70 
Test Cases 
Input  Expected Result 
 5     Table of 5 from 1–10 
 7     Table of 7 from 1–10 
 12    Table of 12 from 1–10 
 0     All results should be 0 
-3     Table of -3 should be displayed 
'''
n = int(input("Enter the number: "))
for i in range(1,11):
  print(n,"X",i,"=",i*n)

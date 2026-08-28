'''
A digital library entrance scans a visitor's age to assign them to the correct section. Write a program that reads an integer visitor_age from input and prints the assigned section name. If the age is less than 13, print 'Kids Area'; if it is between 13 and 19 inclusive, print 'Teen Zone'; otherwise, print 'General Section'.
Input Format: A single integer representing the age.
Output Format: A single string representing the section.
'''
age = int(input("Enter the age: "))

if age<13:
  print("Kids Area")
elif 13 <= age <= 19:
  print("Teen Zone")
else:
  print("General Section")

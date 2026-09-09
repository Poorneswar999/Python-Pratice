'''
A messaging application wants to provide a small text utility that can reverse a user's message.

For example:

Python

should become:

nohtyP

The development team wants the operation to be reusable, so the reverse operation must be implemented inside a function.

Problem Statement

Create a function called reverse_string() that accepts a string and returns the reversed string.

Requirements

• Create a function.
• Accept a string as an argument.
• Return the reversed string.
• Call the function and display the result.

Example Input:

Enter a string: Python

Output:

Reversed String: nohtyP

Test Cases

Input: Python
Expected Output: nohtyP

Input: Hello
Expected Output: olleH

Input: Codegnan
Expected Output: nangedoC

Input: 12345
Expected Output: 54321

Input: Hello World
Expected Output: dlroW olleH

'''
def reverse_string(s):
  return s[::-1]

print("Reversed String:",reverse_string(input("Enter the string: ")))

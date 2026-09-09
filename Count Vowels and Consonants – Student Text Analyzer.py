'''
A school is developing a simple text-analysis tool for students.

The tool should analyze a sentence entered by the student and determine how many vowels and consonants are present.

For example, in:

Python Programming

the program should count the vowels and consonants separately.

Problem Statement

Write a Python program that accepts a string and counts:
• Number of vowels
• Number of consonants

Requirements

• Consider a, e, i, o, u as vowels.
• Handle uppercase and lowercase letters.
• Ignore spaces, numbers, and special characters.
• Use a loop.

Example Input:

Enter a string: Python Programming

Output:

Vowels: 4
Consonants: 13

Test Cases

Input: hello
Expected: Vowels: 2, Consonants: 3

Input: Python
Expected: Vowels: 1, Consonants: 5

Input: Hello World
Expected: Vowels: 3, Consonants: 7

Input: 123
Expected: Vowels: 0, Consonants: 0

Input: Python!
Expected: Vowels: 1, Consonants: 5

Input: AEIOU
Expected: Vowels: 5, Consonants: 0

'''
s = list(input("Enter a string: "))
v = 0
c = 0
for i in s:
  if i.isalpha():
    if i.lower() in ['a','e','i','o','u']:
      v +=1
    else:
      c +=1

print("Vowels:",v,"\nConsonants:",c)
    
    

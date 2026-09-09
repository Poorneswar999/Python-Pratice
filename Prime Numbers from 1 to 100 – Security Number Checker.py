'''
Prime Numbers from 1 to 100 – Security Number Checker

A software company is developing a security application where prime numbers are used for certain internal calculations.

The developer wants to generate all prime numbers between 1 and 100.

A prime number is a number greater than 1 that has exactly two factors: 1 and itself.

Problem Statement

Write a Python program to print all prime numbers between 1 and 100.

Requirements

• Use loops.
• Check whether each number is prime.
• Print only prime numbers.
• Also display the total number of prime numbers found.

Example Output:

Prime numbers between 1 and 100:

2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97

Total Prime Numbers: 25

Test Cases

Range: 1–10
Expected: 2, 3, 5, 7

Range: 1–20
Expected: 2, 3, 5, 7, 11, 13, 17, 19

Range: 1–50
Expected: 15 prime numbers

Range: 1–100
Expected: 25 prime numbers
'''
n = int(input("Enter the max range: "))
noOfPrimes = 0
print("Prime numbers between 1 and",n,": ")
for i in range(2,n+1):
  count = 0
  for j in range(1,i+1):
    if i%j==0:
      count+=1
  if count <= 2:
    print(i)
    noOfPrimes +=1

print("\nTotal Prime Numbers: ",noOfPrimes)

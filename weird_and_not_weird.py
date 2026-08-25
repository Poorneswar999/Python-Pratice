'''
Given an integer,n, perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird

Input: 3
Output: Weird
'''
n = int(input("Enter the n value: "))
if(n % 2 == 1):
    print("Weird")
elif(2<=n<=5):
    print("Not Weird")
elif(6<=n<=20):
    print("Weird")
else:
    print("Not Weird")

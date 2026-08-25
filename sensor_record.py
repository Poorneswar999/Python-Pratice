'''
A sensor records a series of integer readings. Write a program to convert these readings into a tuple and determine the frequency of a specific target value and its first occurrence index. Input Format: The first line contains space-separated integers representing the readings. The second line contains a single target integer. Output Format: Print the count of the target value on the first line and its first index on the second line.
'''
t=tuple(map(int,input().split()))
tar=int(input())
print(t.count(tar))
print(t.index(tar))

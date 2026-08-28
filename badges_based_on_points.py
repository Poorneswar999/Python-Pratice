'''
A digital library assigns membership badges based on a user's accumulated reading points. 
Write a program to read an integer representing points from STDIN and output the corresponding badge name. 
If points are 100 or more, output "Gold"; if 50 to 99, output "Silver"; if 1 to 49, output "Bronze"; and if exactly 0, output "New Member". 
Input Format: A single integer. 
Output Format: A single string.
'''
points = int(input("Enter the points: "))
if points >= 100:
  print("Gold")
elif 50 <= points <= 99:
  print("Silver")
elif 1 <= points <= 49:
  print("Bronze")
else:
  print("New Member")

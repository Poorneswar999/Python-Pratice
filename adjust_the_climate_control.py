'''
A smart home thermostat monitors the current room temperature to adjust the climate control. Write a program that reads an integer temperature and classifies it into a specific category. Output 'Cold' if the temperature is below 15, 'Warm' if it is between 15 and 25 inclusive, and 'Hot' if it is above 25. Input Format: A single integer representing the temperature. Output Format: A single string representing the category.
'''

temp = int(input("Enter the Temperature: "))
if temp < 15:
  print("Cold")
elif temp <= 25:
  print("Warm")
else:
  print("Hot")

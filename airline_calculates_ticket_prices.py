'''
Problem Statement
An airline calculates ticket prices using the following rules:
Base Price = ₹5000
Modifiers:
• Business Seat → +40%
• Premium Economy → +20%
• Economy → No Increase
Booking Days:
• More than 30 days before travel → 10% discount
• Less than 7 days → 25% increase
Season:
• Festival Season → 20% increase
Age:
• Senior Citizen (60+) → 15% discount
Calculate the final ticket price.

Input Format
seat_type
booking_days
festival
age
Output Format
Final Ticket Price
Constraints
1 <= booking_days <= 365
1 <= age <= 100

Test Case 1
Input
Business
40
True
65
Output
6426.0

Test Case 2
Input
Economy
5
False
25
Output
6250.0
'''
seat_type = input("Enter the seat type: ")
booking_days = int(input("Enter the days for booking date: "))
season = input("Is this a festival Season: ")
age = int(input("Enter the age: "))

total_price = 5000

if seat_type == "Business":
    total_price *= 1.4
elif seat_type == "Premium Economy":
    total_price *= 1.2

if booking_days < 7:
    total_price *= 1.25
elif booking_days > 30:
    total_price *= 0.9

if season == "True":
    total_price *= 1.2

if age>60:
    total_price *= 0.85

print("The Final Price is",total_price)

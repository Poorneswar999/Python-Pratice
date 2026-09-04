'''
Build an Employee Bonus Calculator Based on Performance Rating, Experience, and Attendance 
Problem Statement 
A company provides annual bonuses to employees based on their performance rating, years of experience, and attendance percentage. 
Business Rules 
Performance Rating 
• Rating 5 → 25% of salary as bonus  
• Rating 4 → 15% of salary as bonus  
• Rating 3 → 10% of salary as bonus  
• Rating below 3 → No performance bonus  
Experience 
• More than 10 years → Additional 10% of salary  
• Between 5 and 10 years (inclusive) → Additional 5% of salary  
• Less than 5 years → No additional bonus  
Attendance 
• Attendance ≥ 95% → Additional ₹5,000  
• Attendance between 85% and 94% → Additional ₹2,000  
• Attendance below 85% → No attendance bonus  
Calculate the final bonus amount. 
Input Format: 
salary 
performance_rating 
experience attendance 
Output Format: 
Final Bonus Amount 
Constraints 
30000 <= salary <= 2000000 
1 <= performance_rating <= 5 
0 <= experience <= 40 
0 <= attendance <= 100 
Test Case 1:
Input:
80000 
5 
12 
97 
Output: 
33000.0 
Test Case 2: 
Input 
60000 
4 
6 
88 
Output: 
14000.0 
'''
salary = int(input("Enter the salary: "))
performance_rating = int(input("Enter the performance rating: "))
experience = int(input("Enter the experience: "))
attendance = int(input("Enter the attendance: "))
total_bonus = 0

if performance_rating == 5:
  total_bonus += salary * 0.25
elif performance_rating == 4:
  total_bonus += salary * 0.15
elif performance_rating == 3:
  total_bonus += salary * 0.10

if experience > 10:
  total_bonus += salary * 0.10
elif 5 <= experience <= 10:
  total_bonus += salary * 0.05

if attendance >= 95:
  total_bonus += 5000
elif 85 <= attendance < 95:
  total_bonus += 2000

print(total_bonus)

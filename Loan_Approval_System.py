'''
Design a Loan Approval System Using Credit Score, Income, and Existing Liabilities
Problem Statement 
A bank approves loans based on the following criteria: 
Credit Score: 
• Credit Score ≥ 750 → Eligible 
• Credit Score between 650 and 749 → Conditional Eligibility 
• Credit Score < 650 → Rejected 
Income: 
• Monthly Income ≥ ₹50,000 → Eligible 
• Otherwise → Not Eligible 
Liabilities: 
• Existing Liabilities ≤ ₹20,000 → Eligible 
• Otherwise → Not Eligible Decision 
Rules: 
• If all conditions satisfy → Approved 
• If Credit Score is Conditional and other conditions satisfy → Approved with Conditions 
• Otherwise → Rejected 
Input Format :
credit_score 
monthly_income 
existing_liabilities 
Output Format :
Loan Status 
Constraints 300 <= credit_score <= 900 
0 <= monthly_income <= 1000000 
0 <= existing_liabilities <= 500000 
Test Case 1: 
Input: 
780 
60000 
15000 
Output: 
Approved 
Test Case 2: 
Input: 
700 
55000 
18000 
Output: 
Approved with Conditions 
'''
credit_score = int(input("Enter the credit score: "))
monthly_income = int(input("Enter the montly income: "))
existing_liabilities = int(input("Enter the existing liabilities: "))

if credit_score >= 750 and monthly_income >= 50000 and existing_liabilities <= 20000:
  print("Approved")
elif 650 < credit_score < 750 and monthly_income >= 50000 and existing_liabilities <= 20000:
  print("Approved with Conditions")
else:
  print("Rejected")









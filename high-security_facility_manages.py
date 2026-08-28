'''
A high-security facility manages access based on user roles and current emergency status. 
Write a program that grants access if the user is an 'Admin', or if they are 'Staff' with a clearance level of 5 or higher, or if any 'Staff' is present during an emergency. 
For all other roles, access is only granted if it is an emergency and their clearance level is strictly greater than 8. 
Input Format: Three lines containing the Role (string), Clearance Level (integer), and Emergency Status ('True' or 'False'). 
Output Format: Print 'Granted' or 'Denied'.
'''
role = input("Enter the role: ").strip()
level = int(input("Enter the level: ").strip())
emergency = input("Enter the Emergency Status: ").strip()

if role == "Admin":
    print("Granted")
elif role == "Staff":
    if level >= 5 or emergency == "True":
        print("Granted")
    else:
        print("Denied")
else:
    if emergency == "True" and level > 8:
        print("Granted")
    else:
        print("Denied")

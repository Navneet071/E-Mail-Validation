import re

email_conditions ="^ [a-z]+ [\._]?[a-z 0-9]+ [@]\w+ [.]\w{2,3}$"
user_input = input("Enter the email: ")

if re.search(email_conditions, user_input):
    print("Valid Email")
else:
    print("Invalid Email")


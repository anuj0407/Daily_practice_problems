'''
Regex Challenge: Write a regex pattern that validates a simple password. 
It must be 8-12 characters long and contain at least one digit.
'''
import re

pattern = r"^(?=.*\d).{8,12}$"
password = input("Enter a password :")

if re.match(pattern,password):
    print("Valid password")
else:
    print("Invalid password")
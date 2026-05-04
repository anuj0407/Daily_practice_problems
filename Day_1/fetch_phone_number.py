# Regex and List Comprehension
'''
Task: Given a list of strings, 
use list comprehension and regex to extract only the valid 10-digit phone numbers that start with 7, 8, or 9.
'''
import re

data = ["9876543210", "1234567890", "88888-77777", "7123456789", "abc1234567"]
# Expected: ["9876543210", "7123456789"]

valid_phone = r"^[7-9]\d{9}$"
result_list = [string for string in data if re.match(valid_phone,string)] 
print("List of Valid Phone number :",result_list)
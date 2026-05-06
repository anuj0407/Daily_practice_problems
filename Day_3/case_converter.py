'''
The "CamelCase to snake_case" Converter (Regex & Logic)
Task: Write a function that converts a CamelCase string to snake_case using re.sub().
Example: MyDynamicVariable → my_dynamic_variable.
Logical Twist: You need to find the uppercase letters and 
replace them with an underscore followed by the lowercase version, 
but be careful with the very first letter (it shouldn't have an underscore before it).
'''
import re

def camel_case_to_snake_case_converter(text):
    result =  re.sub(r"(?<!^)[A-Z]", lambda match: "_" + match.group(0), text)
    return result.lower()

# example :
text = "MyDynamicVariable"
print(camel_case_to_snake_case_converter(text))


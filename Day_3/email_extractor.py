'''
The "Hidden Email" Extractor (Regex):
Given a messy text like "Contact me at john.doe@gmail.com or support_123@work-place.org", 
write a Regex pattern that extracts all email addresses.
Constraint: Ensure it captures underscores and dots in the username part.
'''
import re

text = "Contact me at john.doe@gmail.com or support_123@work-place.org"
email_pattern = r"[\w.-]+@[\w.-]+\.[a-z]{2,5}"

matches = re.finditer(email_pattern, text)
for m in matches:
    print("Extracted email:", m.group())

'''
The Palindrome Checker
The Logic: A palindrome reads the same forward and backward (e.g., "radar").
The Task: Write a function that takes a string and returns True if it's a palindrome and False otherwise. 
Bonus: Make it ignore spaces and capitalization (e.g., "Race Car" should be True).
'''

def is_pallindrome(text):
    clean_text = text.replace(" ","").lower()
    if clean_text[-1::-1] == clean_text:
        return True
    else :
        return False
    
text = input("Enter a String: ")
if is_pallindrome(text):
    print("String is a pallindrome")
else:
    print("String is not a pallindrome")
'''
Frequency Dictionary (Dict & Loops):
Given a string, create a dictionary where keys are characters and values are their frequencies. 
Then, use Dictionary Comprehension to create a new dictionary containing only the characters that appear more than twice.
'''

text = input("Enter a String: ")
frequency_dict = {}
for char in text:
    if char in frequency_dict:
        frequency_dict[char] = frequency_dict[char]+1
    else:
        frequency_dict[char] = 1

result_dict = {k:v for k,v in frequency_dict.items() if v>2}
print("Dictionary of those character who appear more than twice:",result_dict)
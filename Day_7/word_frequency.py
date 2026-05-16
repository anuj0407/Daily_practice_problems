'''
3. Word Frequency Counter
Goal: Count how many times each word appears in a sentence, ignoring punctuation and casing.
Logic focus: Learning string cleanup with .split() and .strip(), paired with building a frequency map using a dictionary.
Input: "The sky is blue, and the sun is bright."
Output: {'the': 2, 'sky': 1, 'is': 2, 'blue': 1, 'and': 1, 'sun': 1, 'bright': 1}
'''
txt = "The sky is blue, and the sun is bright."
clean_txt = txt.replace(",","").strip(".").lower()
words_list = clean_txt.split()
frequency_counter = {}

for word in words_list:
    if word in frequency_counter:
        frequency_counter[word] += 1
    else:
        frequency_counter[word] = 1

print("Word Frequency Counter:",frequency_counter)
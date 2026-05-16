'''
5. String Compression
Goal: Compress a string by replacing consecutive duplicate characters with the character followed by the count.
If the compressed string isn't shorter, return the original string.
Logic focus: Tracking consecutive character groups and managing string concatenation inside a loop.
Input: "aabcccccaaa"
Output: "a2b1c5a3"
'''
def compress_string(txt):
    if not txt:
        return ""
    compressed = []
    current_char = txt[0]
    count = 1
    for i in range(1, len(txt)):
        if txt[i] == current_char:
            count += 1
        else:
            compressed.append(current_char + str(count))
            current_char = txt[i]
            count = 1
    compressed.append(current_char + str(count))
    result = "".join(compressed)
    return result if len(result) < len(txt) else txt


print(compress_string("aabcccccaaa")) 
print(compress_string("abc"))         

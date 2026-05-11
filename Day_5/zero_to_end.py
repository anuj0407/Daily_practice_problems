'''
Move Zeroes to End
Goal: Given a list of numbers, move all 0s to the end of the list while maintaining the relative order of the non-zero elements.
Input: [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
Constraint: You must do this in-place (modify the original list) without creating a new list.
'''

numbers = [0,1,0,3,12]
count = 0
for num in numbers:
    if num == 0:
        count += 1
        numbers.remove(num)

for i in range(1,count+1):
    numbers.append(0)

print(numbers)
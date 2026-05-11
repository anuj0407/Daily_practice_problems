'''
The "Find the Second Largest" Logic
Goal: Given a list of numbers, find the second largest value. 
Constraint: Do not use list.sort() or max().
Logic: Maintain two variables, largest and second_largest. Update them as you iterate through the list exactly once.
'''

numbers = [2,4,19,35,23,10,27,16]
largest = 0
second_largest = 0
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num 
    elif num > second_largest:
        second_largest = num

print("Second largest number in list :",second_largest)
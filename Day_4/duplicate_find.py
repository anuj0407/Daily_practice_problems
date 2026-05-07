'''
Find the Duplicate
The Logic: Identifying repeated data in a list.
The Task: Given a list of numbers like [1, 3, 4, 2, 2, 5], 
write a script that identifies and prints the first number that appears more than once.
'''

numbers = [1, 3, 4, 2, 2, 5, 5]
unique = set()

for n in numbers:
    if n in unique:
        print(n)
    else:
        unique.add(n)

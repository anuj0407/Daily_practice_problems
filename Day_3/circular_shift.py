'''
The "Circular Shift" List (Logic & Indexing)
Task: Write a function that takes a list and an integer k, then shifts the list to the right by k steps.
Example: [1, 2, 3, 4, 5] shifted by k=2 becomes [4, 5, 1, 2, 3].
Constraint: Try to solve it using List Slicing in just one line.
'''

def circular_shift(num_list,k):
    length = len(num_list)
    return num_list[length-k:length] + num_list[0:length-k]

# example 
num_list = [1, 2, 3, 4, 5]
print(circular_shift(num_list,2))
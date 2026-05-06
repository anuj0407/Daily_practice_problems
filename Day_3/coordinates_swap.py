'''
Tuple Swapping Logic:
You have a list of tuples representing coordinates [(1, 2), (3, 4), (5, 6)]. 
Write a one-liner List Comprehension to swap the X and Y values of each coordinate to get [(2, 1), (4, 3), (6, 5)].
'''

list_of_tuples = [(1, 2), (3, 4), (5, 6)]
print("Original Coordinates list:",list_of_tuples)
result_list = [(y,x) for (x,y) in list_of_tuples ] 
print("Swapped coordinates list:",result_list)
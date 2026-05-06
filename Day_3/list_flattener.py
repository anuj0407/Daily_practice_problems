'''
Nested List Flattener (Comprehension):
Write a list comprehension to flatten a 2D list like [[1, 2], [3, 4], [5]] into [1, 2, 3, 4, 5].
'''

nested_list = [[1, 2], [3, 4], [5]]
flattened_list = [n for sub_list in nested_list for n in sub_list]
print("Flattened 2D list :",flattened_list)
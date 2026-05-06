'''
Unique Element Sum (List & Sets):
Write a function that takes a list of integers and 
returns the sum of only the unique numbers (those that appear exactly once).
'''

def unique_element_sum(element_list):
    unique_list = set(element_list)
    sum = 0
    for element in unique_list:
        sum += element
    return sum

element_list = [2,3,6,2,6,7]
print(unique_element_sum(element_list))
    
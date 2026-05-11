'''
Find the Missing Number (The Math Trick)
Goal: You have a list containing n-1 unique integers in the range from 1 to n.
One number is missing. Find it.
Input: [1, 2, 4, 6, 3, 7, 8] (Here , so 5 is missing).
Constraint: You cannot sort the list.
'''

numbers_list = [1,2,4,6,3,7,8]
n = len(numbers_list)+1
# n(n+1)/2 is the sum of first n numbers 
expected_sum = (n*(n+1))/2
actual_sum = 0
for num in numbers_list:
    actual_sum += num

print("Missing number:",expected_sum - actual_sum)
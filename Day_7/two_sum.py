'''
Two Sum:
Goal: Given a list of numbers and a target number, find the indices of the two numbers that add up to that target.
Logic focus: Moving away from checking every pair (nested loops) to using a single loop and a dictionary to find matches instantly.
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
'''
nums = [2, 7, 11, 15]
target = 9
num_indices = {}
result = []
idx = 0
for num in nums:
    remain = target-num
    if remain in num_indices:
        result = [num_indices[remain],idx]
        break
    num_indices[num] = idx
    idx += 1

if not result :
    print("No match")
else:
    print(result)
'''
2. The Generator Expression
Task: Create a generator expression that yields the squares of even numbers from 1 to 1,000,000. 
Use sys.getsizeof() to compare the memory size of this generator versus a list of the same squares.
'''
import sys

square_generator = (x*x for x in range(1,1000000) if x%2 == 0)
list = [x*x for x in range(1,1000000) if x%2 == 0]

print("Memory consumed by generator:",sys.getsizeof(square_generator))
print("Memory consumed by list:",sys.getsizeof(list))
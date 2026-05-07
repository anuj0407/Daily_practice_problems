'''
The Fibonacci Sequence
The Logic: Every number is the sum of the two preceding ones (0,1,1,2,3,5,8....).
The Task: Write a function that generates the first n numbers of the Fibonacci sequence based on user input.
'''
# Fibonacci for n numbers
# using simple for loop
# def fibonacci_sequence(n):
#     a = 0
#     b = 1
#     for i in range (0, n):
#         print(a,end = " ")
#         temp = b
#         b = a+b
#         a = temp
#     OR
# using recursion
def fibonacci_sequence(n,a=0,b=1):
    if(n<1):
        return 
    print(a, end = " ")
    temp = b
    b = a+b
    a = temp
    fibonacci_sequence(n-1,a,b)

fibonacci_sequence(8)

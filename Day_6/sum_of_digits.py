'''
Sum of Digits: Create a function that calculates the sum of all digits in a number. 
For example, 12345 should return 15 (1+2+3+4+5).
'''

num = int(input("Enter the number:"))
digits = []
while(num>9):
    rem = num%10
    num //= 10
    digits.append(rem)
digits.append(num)
print("Sum of Digits is", sum(digits))

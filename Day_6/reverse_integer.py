'''
Reverse an Integer: Reverse the digits of a given integer while maintaining the sign. 
For instance, -123 becomes -321
'''

number = int(input("Enter the number:"))
sign = -1 if number<0 else 1
reversed_num = 0
number = abs(number)
while(number>0):
    rem = number%10 
    reversed_num = (reversed_num*10) +rem
    number //= 10

print("Reversed number is :",sign*reversed_num)
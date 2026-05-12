'''
Prime Number Check: Write a program to determine if a given integer (e.g., 13) is prime.
'''

number = int(input("Enter the number:"))
flag = True
for i in range(2,number):
    if number % i == 0:
        flag = False

if flag:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
'''
FizzBuzz (The Classic)
Goal: Print numbers from 1 to 50. But for multiples of three print "Fizz", for multiples of five print "Buzz", and for multiples of both print "FizzBuzz". 
Logic: Practice using the modulo operator (%) and careful if-elif ordering.
'''

for i in range(1,51):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)
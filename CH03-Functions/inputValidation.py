'''
# Input Validation
Add try and except statements to the previous project to detect whether the user types in a noninteger string. 
Normally, the int() function will raise a ValueError error if it is passed a noninteger string, as in int('puppy'). 
In the except clause, print a message to the user saying they must enter an integer.
'''

def collatz(number):
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1
    print(number)
    return number

while True:
    print("Please Enter a Positive Number to View its Collatz Sequence: ")
    number = input()
    try:
        number = int(number)
        if number > 0:
            break
    except:
        continue

while number != 1:
    number = collatz(number)
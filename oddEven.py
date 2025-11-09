#Odd or Even

print('This code will determine if the integer is odd or even') #Display message to user

num = int(input('Enter an integer: ')) #get user input

#logic
if num % 2 == 0: #if the number is divided to 2 and the remainder is 0
    print(f'{num} is an even number.')#if it is zero, it is even

else: #since it can only output two values, if it is not even, it must be odd
    print(f'{num} is an odd number.')#if it is not zero and their is a remainder, it is odd
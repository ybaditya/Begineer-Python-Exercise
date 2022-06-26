#The exercise comes first (with a few extras if you want the extra challenge or want to spend more time), 
# followed by a discussion. Enjoy!

#Ask the user for a number. Depending on whether the number is even or odd, 
# print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

#Extras:

#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) and 
# one number to divide by (check). If check divides evenly into num, tell that to the user. 
# If not, print a different appropriate message


numb1 = int(input('Please Input a Number :'))

if numb1 % 4 == 0 :
    print('your Number is EVEN and it can diveded by 4')
elif numb1 % 2 == 0 :
    print('your Number is EVEN')
else :
    print('your Number is ODD')

numb2 = int(input('Please Input a Number (Number):'))
numb3 = int(input('Please Input a Number (Check) :'))

if numb3 % numb2 == 0 :
    print('your number can be divided EVENLY')
else :
    print('your number cant be divided EVENLY')

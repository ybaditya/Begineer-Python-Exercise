

#Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year).
# If you want to do this in a generic way, see exercise 39.

#Extras:

#Add on to the previous program by asking the user for another number 
# and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines. 
# (Hint: the string "\n is the same as pressing the ENTER button)


Name1 = input('Please Input your Name : ')
Age1 = int(input('Please Enter your Age Now : '))

bornyear = 2022 - Age1

year100 = bornyear + 100

print(f'Your Name is {Name1} and in {year100} your age will be 100')

number1 = range(int(input('Enter a Number : ')))

for i in number1 :
    print('\n')
    print(f'Your Name is {Name1} and in {year100} your age will be 100')



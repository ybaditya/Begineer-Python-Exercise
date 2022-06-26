
#Exercise 6 (and Solution)
#Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)

a = input('Please Input a Word : ')

if a == a[::-1] :
    print ('yes')
else :
    print ('no')
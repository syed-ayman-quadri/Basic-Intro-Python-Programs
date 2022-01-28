# Write a Program to check whether a number is a Palindrome or not

num = input('Enter a Number: ')
reverse = num[::-1]
if num == reverse:
    print(f'{num} is a palindrome.')
else:
    print(f'{num} is not a palindrome.')

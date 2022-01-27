# Write a Program to Check Whether a Number is a Perfect Number or Not

num = int(input('Enter the number: '))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i
if sum == num:
    print(f'{num} is a perfect number.')
else:
    print(f'{num} is not a perfect number.')

# Info About Perfect Number
''' In number theory, a perfect number is a positive integer 
    that is equal to the sum of its positive divisors, excluding 
    the number itself. For instance, 6 has divisors 1, 2 and 3 (excluding itself),
    and 1 + 2 + 3 = 6, so 6 is a perfect number. '''
# Write a Program to Check Whether a Number is a Perfect Number or Not

num = int(input('Enter the number: '))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += 1
if sum == num:
    print(f'{num} is a perfect number.')
else:
    print(f'{num} is not a perfect number.')
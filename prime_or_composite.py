# Write a Program to Check if a Number is Prime or Composite

num = int(input('Enter the Number: '))
lim = int(num/2)
if num > 1:
    for i in range(2, lim+1):
        if (num % i) == 0:
            print(f'{num} is a composite number.')
            break
    else:
        print(f'{num} is a prime number.')
else:
    print(f'{num} is neither prime nor composite.')
    
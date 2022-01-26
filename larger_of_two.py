# Write a Program to Enter 2 Numbers and Display The Larger One

num1 = int(input('Enter the First Number: '))
num2 = int(input('Enter the Second Number: '))
if num1 > num2:
    larger = num1
else:
    larger = num2
print(f'The larger number from {num1} and {num2} is {larger}.')
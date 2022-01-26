# Write a Program to Enter 3 Numbers and Display the Larger Number

num1 = int(input('Enter The First Number: '))
num2 = int(input('Enter The Second Number: '))
num3 = int(input('Enter The Third Number: '))
if num1 > num2 and num1 > num3:
    larger = num1
elif num2 > num1 and num2 > num3:
    larger = num2
else:
    larger = num3
print(f'The larger number from {num1}, {num2} & {num3} is {larger}.')
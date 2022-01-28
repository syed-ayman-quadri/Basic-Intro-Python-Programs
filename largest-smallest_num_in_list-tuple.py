# Write a Program to Find the Largest and Smallest Number in a List/Tuple

L = eval(input('Enter the List/Tuple: '))
min = L[0]
max = L[0]
for i in L:
    if i > max:
        max = i
    elif i < min:
        min = i
print(f'Minimum = {min}')
print(f'Maximum = {max}')
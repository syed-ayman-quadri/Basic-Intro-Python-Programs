# Write A Program To Check Whether A Number Is An Armstrong Number or Not

num = int(input('Enter the Number: '))
l = len(str(num))
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit**l
    temp = temp // 10
if sum == num:
    print(f'{num} is an Armstrong Number.')
else:
    print(f'{num} is not an Armstrong Number.')

# (temp) means temporary.
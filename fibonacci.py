# Write a Program To Print The Fibonacci Series Upto First n Elements

num = int(input('Enter the Number of Terms: '))
a = 0
b = 1
print(a, end=' ')
print(b, end=' ')
for i in range(2, num):
    c = a+b
    print(c, end=' ')
    a, b = b, c
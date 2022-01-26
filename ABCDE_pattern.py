# Write a Program to Print The Folowing Pattern
'''A
   A B
   A B C
   A B C D
   A B C D E '''

n = int(input('Enter the Number of Rows: '))
k = 0
for i in range(1, n+1):
    k = 65
    for j in range(1, i+1):
        print(chr(k), end=' ')
        k += 1
    print()
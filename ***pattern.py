# Write a Program To Print The Following Pattern
'''*
   * *
   * * *
   * * * *'''

n = int(input('How many rows of the pattern do you want? '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*', end=' ')
    print()
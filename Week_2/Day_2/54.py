# Print numbers until the user enters 0
n = int(input('Enter a number: '))

# iterate until the user enters 0
while n != 0:
    print(f'You entered {n}.')
    n = int(input('Enter a number: '))

print('The end.')

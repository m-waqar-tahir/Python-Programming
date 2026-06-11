# Reverse half pyramid printing using * and numbers
rows = int(input("Enter number of rows: ")) # To input number of rows

for i in range(rows, 0, -1): # Here (-1) is step size, and range falls between number of given rows and runs backwards.
    for j in range(0, i):
        print("* ", end=" ")
    
    print()

for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    
    print()
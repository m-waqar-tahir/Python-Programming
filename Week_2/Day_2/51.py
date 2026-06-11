# To print full pyramid using * and numbers
rows = int(input("Enter number of rows: "))

j = 0

for i in range(1, rows+1):
    for k in range(1, (rows-i)+1):
        print(end="  ")
   
    while j != (2*i-1):
        print("* ", end="")
        j += 1
    j = 0
    print()
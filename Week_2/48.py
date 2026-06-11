# To print ordered letters from their ASCII numbers using while loop
rows = int(input("Enter number of rows: "))
i = 65
count = 0
while count < rows:
    print(chr(i))
    i += 1
    count += 1
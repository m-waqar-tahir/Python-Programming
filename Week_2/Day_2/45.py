# Program to print half pyramid using *

rows = int(input("Enter number of rows: "))

print(range(rows))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print()
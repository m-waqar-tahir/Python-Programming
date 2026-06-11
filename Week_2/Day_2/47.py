# To print ordered letters from their ASCII numbers

rows = int(input("Enter number of rows: "))
for i in range(rows):
    print(f"At number {65+i}:", chr(65 + i))

# Output:
# At number 65: A
# At number 66: B
# At number 67: C
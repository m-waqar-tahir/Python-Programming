# ============================================================
# Program: Half Pyramid using Alphabets
# Pattern:
# A
# A B
# A B C
# ============================================================

# Take number of rows from user and convert to integer
rows = int(input("Enter number of rows: "))

# ----------------------
# Method 1: Using for loop
# ----------------------

for i in range(rows):            # Outer loop: runs once for each row
    ascii_value = 65             # Reset ASCII to 65 (A) at start of every row
    for j in range(i + 1):      # Inner loop: runs i+1 times per row
        alphabet = chr(ascii_value)       # Convert ASCII value to character
        print(alphabet, end=" ")          # Print character on same line
        ascii_value += 1                  # Move to next letter
    print()                      # Move to next line after each row

# ----------------------
# Method 2: Using while loop
# ----------------------

counter = 0                      # Initialize outer counter to track current row

while counter < rows:            # Outer loop: runs until all rows are printed
    ascii_value = 65             # Reset ASCII to 65 (A) at start of every row
    inner = 0                    # Initialize inner counter for current row

    while inner <= counter:      # Inner loop: runs counter+1 times per row
        print(chr(ascii_value), end=" ")  # Convert ASCII to character and print
        ascii_value += 1                  # Move to next letter
        inner += 1                        # Increment inner counter

    print()                      # Move to next line after each row
    counter += 1                 # Increment outer counter to move to next row
# Full pyramid inverted

rows = int(input("Enter number of rows: "))

# outer loop controls each row, i = 1, 2, 3 ... rows
for i in range(1, rows + -1):

    # PART 1: SPACES
    # row 1 gets most spaces, last row gets none
    # example: rows=4, i=1 => 3 spaces, i=2 => 2 spaces, i=4 => 0 spaces
    for space in range(rows - i):
        print("  ", end="")        # end="" means stay on same line

    # PART 2: ASCENDING NUMBERS (going up)
    # i=1 => prints: 1
    # i=2 => prints: 2 3
    # i=3 => prints: 3 4 5
    # i=4 => prints: 4 5 6 7
    for j in range(i, 2 * i):
        print(j, end=" ")

    # PART 3: DESCENDING NUMBERS (going down, mirror of ascending)
    # we skip the peak number to avoid printing it twice
    # i=1 => prints: nothing  (no mirror needed)
    # i=2 => prints: 2
    # i=3 => prints: 4 3
    # i=4 => prints: 6 5 4
    for j in range(2 * i - 2, i - 1, 1):
        print(j, end=" ")

    # PART 4: NEW LINE
    # after each row is complete, move to next line
    print()
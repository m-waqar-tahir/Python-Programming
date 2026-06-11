# To print half pyramid a using numbers

rows = int(input("Enter number of rows: "))

print(range(rows))
for i in range(rows):
    print(f"After iteration {i +1}:", range(i + 1)) # For understanding how inner loop works
    for j in range(i + 1):
       print(j+1, end=" ")
    print()

# Output:
# Enter number of rows: 3 / You can input any number of rows
# After iteration 1: range(0, 1)
# 1
# After iteration 2: range(0, 2)
# 1 2
# After iteration 3: range(0, 3)
# 1 2 3
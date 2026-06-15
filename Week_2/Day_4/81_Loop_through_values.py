# Loop through values in a dictionary to print all values present in a dictionary.

student = {"name": "Waqar", "age": 25}

print("Using for loop:")
for value in student.values():
    print(value)

i = 0

print("\nUsing while loop:")
while i < len(student):
    print(list(student.values())[i])  # Converted to a list to use the [i] index
    i = i + 1

# Output:
# Using for loop:
# Waqar
# 25

# Using while loop:
# Waqar
# 25
# Slice parts of a string using the slice operator [start:stop:step]
my_string = "Hello, Waqar Tahir!"
print("The sliced string is:", my_string[0:5]) 
print("The sliced string is:", my_string[7:12]) 
print("The sliced string is:", my_string[0:19:2])

# You can also omit the start, stop, or step parameters to use their default values
print("\nThe sliced string is:", my_string[:5])  # From the beginning to index 5
print("The sliced string is:", my_string[7:])   # From index 7 to the end
print("The sliced string is:", my_string[::2])  # Every second character from the entire string

# Negative indexing can also be used in slicing
print("\nThe sliced string is:", my_string[-6:])  # Last 6 characters

# You can also reverse a string using slicing
print("\nThe reversed string is:", my_string[::-1])  # Reverses the entire string

# Output:
# The sliced string is: Hello
# The sliced string is: Waqar
# The sliced string is: Hlo aa ai!

# The sliced string is: Hello
# The sliced string is: Waqar Tahir!
# The sliced string is: Hlo aa ai!

# The sliced string is: Tahir!

# The reversed string is: !rihaT raqaw ,olleH
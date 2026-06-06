# Join two or more strings together using the + operator
first_name = "Waqar"
last_name = "Tahir"
full_name = first_name + " " + last_name
print("The full name is:", full_name)

# Using the join() method to concatenate a list of strings
words = ["I", "am", "enjoying", "working", "with", "Python"]
sentence = " ".join(words)
print("\nThe concatenated sentence is:", sentence)

# Using f-strings for string concatenation
age = 25
print(f"\nMy name is {full_name} and I am {age} years old.")
# Using the format() method for string concatenation
print("My name is {} and I am {} years old.".format(full_name, age))

# Using the % operator for string concatenation
print("My name is %s and I am %d years old." % (full_name, age))

# Concatenating strings with numbers (need to convert numbers to strings)
number_of_cats = 3
print(f"\nI have {number_of_cats} cats.")
print("I have {} cats.".format(number_of_cats))
print("I have %d cats." % (number_of_cats))

# Output:
# The full name is: Waqar Tahir

# The concatenated sentence is: I am enjoying working with Python

# My name is Waqar Tahir and I am 25 years old.
# My name is Waqar Tahir and I am 25 years old.
# My name is Waqar Tahir and I am 25 years old.

# I have 3 cats.
# I have 3 cats.
# I have 3 cats.
# Conversion of string cases
string = "I AM LEARning PytTHON"
print("Original string:", string)

print("Uppercase:", string.upper())
print("Lowercase:", string.lower())

# Convert to title case
print("Title case:", string.title())

# Convert to sentence case
print("Sentence case:", string.capitalize())

# Check if the string is in uppercase or lowercase
print("The string is in uppercase?", string.isupper())
print("The string is in lowercase?", string.islower())

# Convert to swap case
print("Swap case:", string.swapcase())

# Convert to casefold (for case-insensitive comparisons)
print("Casefold:", string.casefold())

# Check if the string is in title case
print("The string is in title case?", string.istitle())

# Check if the string is in sentence case
print("The string is in sentence case?", string[0].isupper() and string[1:].islower())

# Output:
# Original string: I AM LEARning PytTHON
# Uppercase: I AM LEARNING PYTHON
# Lowercase: i am learning python
# Title case: I Am Learning Python
# Sentence case: I am learning python
# The string is in uppercase? False
# The string is in lowercase? False
# Swap case: i am LEARNING pYTTHON
# Casefold: i am learning python
# The string is in title case? False
# The string is in sentence case? False
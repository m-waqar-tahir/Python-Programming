# String splitting
s = "Python is learning me."
print(f"\nOriginal string: \"{s}\"")

# Split the string into a list of substrings
words = s.split()
print(f"\nAfter splitting: {words}")

# Split by a specific delimiter
s1 = "apple,banana,cherry"
fruits = s1.split(",")
print(f"\nAfter splitting by comma: {fruits}")

# Split into a maximum of n substrings
s2 = "one-two-three-four"
parts = s2.split("-", 2)
print(f"\nAfter splitting by '-' with maxsplit=2: {parts}")
# Split by whitespace and remove extra spaces
s3 = "   Hello   World   "
cleaned = s3.split()
print(f"\nAfter splitting and removing extra spaces: {cleaned}")
# Split by newline character
s4 = "Line 1\nLine 2\nLine 3"
lines = s4.split("\n")
print(f"\nAfter splitting by newline: {lines}")
# Split by a specific character and keep the delimiter
s5 = "key=value;key2=value2"
key_value_pairs = s5.split(";")
print(f"\nAfter splitting by ';': {key_value_pairs}")

# Output:
# Original string: "Python is learning me."
# After splitting: ['Python', 'is', 'learning', 'me.']
# After splitting by comma: ['apple', 'banana', 'cherry']
# After splitting by '-' with maxsplit=2: ['one', 'two', 'three-four']
# After splitting and removing extra spaces: ['Hello', 'World']
# After splitting by newline: ['Line 1', 'Line 2', 'Line 3']
# After splitting by ';': ['key=value', 'key2=value2']
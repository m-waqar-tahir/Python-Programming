# String joining
words = ["Python", "is", "learning", "me."]
s = " ".join(words)
print(f"\nAfter joining: \"{s}\"")

# Join a list of strings with a specific delimiter
fruits = ["apple", "banana", "cherry"]
s1 = ",".join(fruits)
print(f"\nAfter joining by comma: \"{s1}\"")

# Join with a newline character
lines = ["Line 1", "Line 2", "Line 3"]
s2 = "\n".join(lines)
print(f"\nAfter joining by newline as a multiline string: \"{s2}\"")

# Join with an empty string (concatenation)
chars = ["W", "a", "q", "a", "r"]
s3 = "".join(chars)
print(f"\nAfter joining with an empty string: \"{s3}\"")

# Output:
# After joining: "Python is learning me."
# After joining by comma: "apple,banana,cherry"
# After joining by newline as a multiline string: "Line 1\nLine 2\nLine 3"
# After joining with an empty string: "Waqar"
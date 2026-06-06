# String stripping
s = "       I AM LEARning PytTHON      "
print(f"\nOriginal string: \"{s}\"")

print(f"Left strip: \"{s.lstrip()}\"")
print(f"Right strip: \"{s.rstrip()}\"")
print(f"Both strips: \"{s.strip()}\"")

# Stripping specific characters
s2 = "###Hello, World!###"
print(f"\nOriginal string: \"{s2}\"")
print(f"Strip '#' characters: \"{s2.strip('#')}\"")

# Stripping whitespace and specific characters
s3 = "   ***Python is great!***   "
print(f"\nOriginal string: \"{s3}\"")
print(f"Strip whitespace and '*' characters: \"{s3.strip(' *')}\"")

# Stripping characters from the left and right
s4 = ">>>Welcome to Python<<<"
print(f"\nOriginal string: \"{s4}\"")
print(f"Strip '>' and '<' characters: \"{s4.strip('><')}\"")

# Output:
# Original string: "       I AM LEARning PytTHON      "
# Left strip: "I AM LEARning PytTHON        "   
# Right strip: "       I AM LEARning PytTHON"
# Both strips: "I AM LEARning PytTHON"

# Original string: "###Hello, World!###"
# Strip '#' characters: "Hello, World!"

# Original string: "   ***Python is great!***   "
# Strip whitespace and '*' characters: "Python is great!"

# Original string: ">>>Welcome to Python<<<"
# Strip '>' and '<' characters: "Welcome to Python"
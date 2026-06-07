# String counting number of times a word appears in a string
s = "The quick brown fox jumps over the lazy dog. The dog was really lazy."
word = "lazy"
print(s.count(word))  # 2

# String counting number of times a word appears in a string, case insensitive
s = "The quick brown fox jumps over the Lazy dog. The dog was really lAZY."
word = "lazy"
print(s.lower().count(word.lower()))  # 2
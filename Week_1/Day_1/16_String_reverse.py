# String reverse
s = "I am tired learning Python"
print(s[::-1])

# Substring reverse
print(s[5:11][::-1])

# Reverse each word in the string
words = s.split()
reversed_words = [word[::-1] for word in words]
print(" ".join(reversed_words))

# Output:
# nohtyP gninrael derit ma I
# derit
# I ma derit gninrael nohtyP
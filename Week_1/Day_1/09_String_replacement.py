# String replacement
s = "I am learning Java"
print(f"\nOriginal string: \"{s}\"")

# Replace a substring
s = s.replace("Java", "Python")
print(f"\nAfter replacing 'Java' with 'Python': \"{s}\"")

# Replace multiple occurrences
s1 = "Hello, World! Hello, Python!"
s1 = s1.replace("Hello", "Hi")
print(f"\nAfter replacing 'Hello' with 'Hi': \"{s1}\"")

# --- Setup your original string ---
original_str = "Waqar is a good boy. Waqar likes to play cricket. Waqar is learning python."

# 1. Replace only the FIRST occurrence
s2 = original_str.replace("Waqar", "He", 1)
print(f"\nAfter replacing only the first occurrence of 'Waqar' with 'He': \"{s2}\"")

# --- RESET s2 so the first change doesn't interfere ---
s2 = original_str

# 2. Replace only the LAST occurrence
s2 = s2[::-1].replace("raqaW", "eH", 1)[::-1]
print(f"\nAfter replacing only the last occurrence of 'Waqar' with 'He': \"{s2}\"")

# 3. Replace ALL occurrences
s2 = original_str.replace("Waqar", "He")
print(f"\nAfter replacing all occurrences of 'Waqar' with 'He': \"{s2}\"")

# Output:
# Original string: "I am learning Java"
# After replacing 'Java' with 'Python': "I am learning Python"
# After replacing 'Hello' with 'Hi': "Hi, World! Hi, Python!"
# After replacing only the first occurrence of 'Waqar' with 'He': "He is a good boy. Waqar likes to play cricket. Waqar is learning python."
# After replacing only the last occurrence of 'Waqar' with 'He': "Waqar is a good boy. Waqar likes to play cricket. He is learning python."
# After replacing all occurrences of 'Waqar' with 'He': "He is a good boy. He likes to play cricket. He is learning python."
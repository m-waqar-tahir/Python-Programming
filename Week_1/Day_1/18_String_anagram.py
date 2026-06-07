# String anagram
s1 = "listen"
s2 = "silent"
s1_sorted = sorted(s1)
s2_sorted = sorted(s2)
print(s1_sorted)  # ['e', 'i', 'l', 'n', 's', 't']
print(s2_sorted)  # ['e', 'i', 'l', 'n', 's', 't']
print(s1_sorted == s2_sorted)  # True
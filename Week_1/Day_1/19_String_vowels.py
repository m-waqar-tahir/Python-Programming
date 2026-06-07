# String vowels
s = "Waqar loves boxing."
vowels = "aeiou"
no_of_vowels = 0
for i in s:
    if i in vowels:
        no_of_vowels += 1
print(no_of_vowels)  # 2
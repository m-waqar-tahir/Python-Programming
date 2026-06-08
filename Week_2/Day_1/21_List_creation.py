# List creation, insertion, and extension

# 1. Using square brackets
my_list = [1, 2, 3, 4, 5]
print(my_list)

# Output: [1, 2, 3, 4, 5]

# 2. Using the list() constructor
my_list = list((1, 2, 3, 4, 5))
print(my_list)

# Output: [1, 2, 3, 4, 5]

# 4. Using the range() function
my_list = list(range(1, 6))
print(my_list)

# Output: [1, 2, 3, 4, 5]

# 5. Using the split() method from a string
my_string = "1 2 3 4 5"
my_list = my_string.split()  # This will split the string into a list of strings
print(my_list)

# Output: ['1', '2', '3', '4', '5']

# 6. Using the list() constructor with a string
my_string = "My name is Waqar Tahir"
my_list = my_string.split()
appended = list(my_string)
print(" ".join(my_list))

# Output: ['My', 'name', 'is', 'Waqar', 'Tahir']

# 7. To show list items into a the same list in sentences form and keep in the list type as one item
spearate_words_list = ['My', 'name', 'is', 'Waqar', 'Tahir']
new_list = " ".join(spearate_words_list)
sentence_as_item_in_list = [new_list]
print(sentence_as_item_in_list)

# Output: ['My name is Waqar Tahir']
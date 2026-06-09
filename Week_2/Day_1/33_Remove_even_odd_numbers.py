# Remove even and odd numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = [i for i in numbers if i % 2 != 0]
even_numbers = [i for i in numbers if i % 2 == 0]
print("Odd numbers:", odd_numbers)  # Output: [1, 3, 5, 7, 9]
print("Even numbers:", even_numbers)  # Output: [2, 4, 6, 8, 10]
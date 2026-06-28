# Arbitrary arguments in a function

def F1(*fruits): # In cases we want to take multiple arguments into one parameter, a star symbol is put on left of the parameter.
                 # This is called Arbitrary arguments.
    print(type(fruits)) # type() function is used to check what type of data is stored into a variable or parameter in case of function.
    print(fruits) 

F1("Apple", "Guawa", "Orange") # One thing to be considered is that multiple arguments will be put into the parameter not as a list of items.
                               # But in the form of a tuple.
    
    # This is because, square brackets([]) around the items make them a list.
    # But in case of items with no any brackets are considered as Tuple in Python.
    # 
# Output:
# ('Apple', 'Guawa', 'Orange') 
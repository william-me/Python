my_tuple = (1, 2, 3, 4, 5)

#tuple indexing
first_element = my_tuple[0]
print(first_element) # Output: 1

#tuple length
tuple_length = len(my_tuple)
print(tuple_length) # Output: 5

#tuple unpacking
cordinates = (4, 6)
x, y = cordinates
print(x, y) # Output: 4 6

#concatenate tuples
new_tuple = my_tuple + (6, 7)
print(new_tuple) # Output: (1, 2, 3, 4, 5, 6, 7)

#checking for an element in a tuple
is_present = 5 in my_tuple
print(is_present) # Output: True

#tuple for multiple values
def get_coordinates():
    return (4, 6)
x, y = get_coordinates()
print(x, y) # Output: 4 6

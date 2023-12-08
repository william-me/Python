#lists
my_list = [1, 2, 3, 'banana', 'apple']

#list indexing
first_element = my_list[0] #Accessing   first element

#list length
list_length = len(my_list) #Accessing list length

my_list.append(4) #Adding element to the end of the list

#list removing
my_list.remove('banana') #Removes banana element from the list

#list slicing
subset = my_list[1:3] #Accessing elements at index 1 and 2]
print(subset) #Output [2, 3]

#list concatenation
new_list = my_list + [5, 6] #Concatenating my_list with [5, 6]
print(new_list)

#list sorting
my_list.sort() #Sorts the list in ascending order

is_present = 'banana' in my_list #Checks if banana is present in the list
print(is_present) #Output: False
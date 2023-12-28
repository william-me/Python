# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
my_set = {1, 2, 3, 4, 5}

#add and remove elements to the set
my_set.add(6)
my_set.remove(5)

#set operations
set1 = {1, 2, 3}
set2 = {4, 5, 6}
union_set = set1.union(set2) #Output {1, 2, 3, 4, 5, 6}
intersection_set = set1.intersection(set2) #
set_diffrence = set1.difference(set2) #

print(union_set) #Output {1, 2, 3, 4, 5, 6}

is_subset = set1.issubset(set2) #check if set1 is a subset of set2
is_superset = set1.issuperset(set2) #check if set1 is a superset of set2
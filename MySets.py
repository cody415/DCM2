my_set = {10, 20, 30, 40, 50}

print("Original set:", my_set)

my_set.add(60)
print("After adding 60:", my_set)

my_set.remove(20)
print("After removing 20:", my_set)

set2 = {40, 50, 60, 70, 80}

print("Union:", my_set.union(set2))
print("Intersection:", my_set.intersection(set2))
print("Difference:", my_set.difference(set2))

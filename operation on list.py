fruits = ["Mango", "Apple", "Banana", "Orange", "Grapes"]

print("My favourite fruits are:", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

fruits.append("Pineapple")
print("After adding Pineapple:", fruits)

fruits.insert(2, "Strawberry")
print("After inserting Strawberry at position 2:", fruits)

fruits.remove("Banana")
print("After removing Banana:", fruits)

fruits.sort()
print("Sorted fruits:", fruits)

fruits.reverse()
print("Reversed fruits:", fruits)

print("Total number of fruits:", len(fruits))

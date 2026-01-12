data = {
    "name": "John",
    "age": 25,
    "course": "Mathematics",
    "grade": "B",
    "city": "New York"
}

print("Dictionary:", data)
print("Name:", data["name"])

data["email"] = "john@example.com"
print("After adding email:", data)

data["grade"] = "A"
print("After updating grade:", data)

data.pop("city")
print("After removing city:", data)

print("Keys:", data.keys())
print("Values:", data.values())
print("Items:", data.items())
print("Total entries:", len(data))

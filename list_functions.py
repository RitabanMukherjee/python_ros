lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]

friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1, "Kelly")
friends.remove("Jim")
friends.pop() # removes last element in the list


print(friends)
print(friends.index("Kevin"))
print(friends.count("Jim"))

print(friends)

friends2 = friends.copy()
print(friends2)
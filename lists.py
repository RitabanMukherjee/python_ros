friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"] #Python lists can have a mixture of strings, numbers and booleans
print(friends)
print(friends[1])
print(friends[-1]) # negative indices start at the back of the list. negative indices start at -1 not 0
print(friends[1:]) 
print(friends[1:3])

friends[1] = "Mike"
print(friends)
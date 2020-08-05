#for letter in "Giraffe Academy":
#    print(letter)

friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)

len(friends) #prints number of elements in array

#for index in range(10):
#    print(index)

for index in range(3,10):  #last value in range not included
    print(index)

for index in range(len(friends)):
    print(friends[index])


for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("Not first")
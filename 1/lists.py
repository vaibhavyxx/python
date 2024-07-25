#list- how to add, access and remove data
friends = ["Sally", "Mango", "Doreamon"]
print(friends)
friends[2] = "X"
print(friends)
print(friends[-1])
acquaintances = ["sookie", "vedetta"]
friends.extend(acquaintances)
print(friends)
friends.append("henry")
print(friends)
friends.insert(1, "aussue")
print(friends)
#friends.clear()
print(friends.count("X"))
friends.sort()
print(friends)

#uppercase has a higher priority than lowercase in sort
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)






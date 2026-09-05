# Program 1
cart = ["Laptop", "Mouse", "Keyboard"]
cart.append("Moniter")
cart.pop(1)
for i in cart:
 print(i)

print(len(cart))
#-----------------------------------

#program 2
user = {
    "name": "Sam",
    "age": 22,
    "role": "Developer",
    "is_active": True
}
print("Name", user["name"])
print("Age", user["age"])
print("Role", user["role"])
print("Active", user["is_active"])

#---------------------
#program 3
orders = [101, 102, 101, 103, 102, 104, 103]
x=set(orders)
print(x)


#---------------------
#program 4
prices = [100, 250, 500, 750]
x=[x for x in prices if x>=500]
print(x)

#---------------------
#program 5
users = [
    {"name": "Sam", "age": 22, "role": "Developer"},
    {"name": "John", "age": 27, "role": "Tester"},
    {"name": "Alex", "age": 30, "role": "Manager"},
    {"name": "Mike", "age": 24, "role": "Developer"}
]

for user in users:
    print(user["name"]+"-"+str(user["age"])+"-"+user["role"])
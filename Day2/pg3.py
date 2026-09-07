def registor_user(name, age):

    if age < 18:
        raise ValueError("User must be 18 or older")

    print("User " + name + " registered successfully")


name = input("Enter the name: ")
age = int(input("Enter age: "))

try:
    registor_user(name, age)
except ValueError as e:
    print("Error:", e)
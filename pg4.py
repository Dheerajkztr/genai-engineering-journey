users=[]
def reg_user(name,age,role):
    if(age<18):
        raise ValueError("Age is Below 18")
    x={
        "name":name,
        "age":age,
        "role":role
    }
    users.append(x)
    return users
    
i=0
while i in range(2):
 try:
    name=input("Enter your name : ")
    age=int(input("Enter Age : "))
    role=input("Enter Role :")
    users=reg_user(name,age,role)
    i=i+1
 except ValueError as e:
    print("Error ", e)

for user in users:
    print(
        "Name:", user["name"],
        "Age:", user["age"],
        "Role:", user["role"]
    )
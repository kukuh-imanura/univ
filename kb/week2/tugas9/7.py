user = {
    "nama" : "Narto",
    "age" : 20
}

nama = user["nama"]
print(nama)

username = user.get("username")
print(username)

username = user.get("username", "Narto123")
print(username)
print(user)

user["username"] = "Narto321"
print(user)

user["nama"] = "Naru"
print(user)
file = open("file.txt", "a")
print(file.readable())
print(file.writable())

file.write("Sakura-sakra123-19")

file.close()

file = open("text.txt", "w")

file.write("Hello World")

file.close()
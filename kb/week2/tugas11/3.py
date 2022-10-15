file = open("file.txt", "r")

print(file.readline())
# print(file.read())

line = file.readlines()

for l in line :
    print(l)

file.close()
msg = input(">>> ")

map = {
    ":)" : "😊",
    ":|" : "😐",
    "XD" : "😆"
}

words = msg.split(" ")

out = ""
for w in words :
    out = out + map.get(w, w) + " "

print(out)
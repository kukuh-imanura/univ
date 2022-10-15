import csv

with open("file.csv") as file :
    csv = csv.reader(file, delimiter=",")

    for c in csv :
        print(f"Nama : {c[0]}\nUsername : {c[1]}\nUmur : {c[-1]}")
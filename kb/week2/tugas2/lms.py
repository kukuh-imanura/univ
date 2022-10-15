from math import sqrt

a = input("Masukkan Nilai A : ")
t = input("Masukkan Tinggi : ")

a = int(a)
t = int(t)

z = ((a/2)**2) + (t**2)
# print(z)

b = sqrt(z)
# print(b)

ls = (a*b)/2
la = a*a

ll = (4*ls) + (la)
v = (la * t)/3

print(f"Luas Limas : {ll}")
print(f"Volume Limas : {v}")
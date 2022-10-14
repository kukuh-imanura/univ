phi = float(22) / 7
print("Masukkan Radius : ", end='', flush=True)
r = int(input())
print("Masukkan Tinggi : ", end='', flush=True)
t = int(input())
print("Masukkan S : ", end='', flush=True)
s = int(input())
l = phi * r * s + phi * r * r
v = float(phi * r * r * t) / 3
print("Luas Permukaan : " + str(l))
print("Volume: " + str(v))

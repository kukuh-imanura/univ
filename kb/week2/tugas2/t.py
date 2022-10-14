phi = float(22) / 7
print("Masukkan Radius : ", end='', flush=True)
r = int(input())
print("Masukkan Tinggi : ", end='', flush=True)
t = int(input())
l = 2 * phi * r * t + 2 * phi * r * r
v = phi * r * r * t
print("Luas Permukaan : " + str(l))
print("Volume: " + str(v))

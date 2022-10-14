phi = float(22) / 7
print("Masukkan Radius : ", end='', flush=True)
r = int(input())
l = 4 * phi * r * r
v = float(l * r) / 3
print("Luas Permukaan : " + str(l))
print("Volume: " + str(v))

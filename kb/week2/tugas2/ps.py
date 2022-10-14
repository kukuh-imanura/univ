print("Masukkan Panjang : ", end='', flush=True)
p = int(input())
print("Masukkan Sisi : ", end='', flush=True)
s = int(input())
print("Masukkan Tinggi : ", end='', flush=True)
t = int(input())
l = 3 * s * p + s * t
v = float(s * t * p) / 6
print("Luas Permukaan : " + str(l))
print("Volume: " + str(v))

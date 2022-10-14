print("Masukkan Waktu (Menit) : ", end='')
w = int(input())
print("Masukkan Kecepatan (Km/h) : ", end='')
k1 = int(input())
k2 = float(k1 * 1000) / 60
print("Kecepatan : " + str(k2) + "M/m")
j = k2 * w
print("Jarak : " + str(j) + "Meter")

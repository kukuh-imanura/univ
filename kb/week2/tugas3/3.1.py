print("Masukkan Kecepatan (Km/h) : ", end='', flush=True)
k1 = int(input())
k2 = float(k1) / 60
print("Kecepatan : " + str(k2) + "Km/m")
print("Masukkan Jarak (Km) : ", end='', flush=True)
j = int(input())
w = float(j) / k2
print("Waktu : " + str(w) + "Menit")

print("Masukkan Jumlah (M3) : ", end='', flush=True)
j1 = int(input())
j2 = j1 * 1000
print("Jumlah : " + str(j2) + "Liter")
print("Masukkan Waktu (Jam) : ", end='', flush=True)
w1 = int(input())
w2 = w1 * 3600
print("Waktu : " + str(w2) + "Detik")
d = float(j2) / w2
print("Debit : " + str(d) + "Liter/s")

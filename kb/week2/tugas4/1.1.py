print("Masukkan Jumlah : (Liter) ", end='', flush=True)
j1 = int(input())
j2 = j1 * 1000
print("Jumlah : " + str(j2) + "Cm3")
print("Masukkan Waktu (Menit) : ", end='', flush=True)
w1 = int(input())
w2 = w1 * 60
print("Waktu : " + str(w2) + "Detik")
d = float(j2) / w2
print("Debit : " + str(d) + "cm3/s")

print("Input Debit : (M3/s) ", end='', flush=True)
d1 = int(input())
d2 = float(d1 * 1000) / 60
print("Debit : " + str(d2) + "L/m")
print("Input Waktu : (Menit) ", end='', flush=True)
w = int(input())
j = d2 * w
print("Jumlah : " + str(j) + "Liter")

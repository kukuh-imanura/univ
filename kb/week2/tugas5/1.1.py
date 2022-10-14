print("Masukkan Jarak Peta (cm) : ", end='', flush=True)
p = int(input())
print("Masukkan Jarak Sebenarnya (Km) : ", end='', flush=True)
j1 = int(input())
j2 = j1 * 100000
print("Jarak Sebenarnya : " + str(j2) + "cm")
s = float(j2) / p
print("Skala 1 : " + str(s) + "cm")

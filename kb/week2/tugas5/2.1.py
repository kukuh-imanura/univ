print("Masukkan Skala (cm) 1 : ", end='', flush=True)
s = int(input())
print("Masukkan Jarak Peta (cm) : ", end='')
p = int(input())
j1 = s * p
print("Jarak : " + str(j1) + "cm")
j2 = float(j1) / 100000
print("Jarak : " + str(j2) + "Km")

import sys


print("KALKULATOR")
print("==============================")
print()

print("Masukkan Operasi (+,-,*,/): ", end='')
operasi = str(input())

print("Masukkan Nilai Pertama: ", end='')
a1 = int(input())

print("Masukkan Nilai Kedua: ", end='')
a2 = int(input())

if operasi == "+" :
    hasil = a1 + a2
elif operasi == "-" :
    hasil = a1 - a2
elif operasi == "*" :
    hasil = a1 * a2
elif operasi == "/" :
    hasil = a1/a2
else :
    print("Operasi Tidak Ada")
    print()
    sys.exit()

print("Hasil dari " +str(a1) +str(operasi) +str(a2) +" adalah : " +str(hasil))
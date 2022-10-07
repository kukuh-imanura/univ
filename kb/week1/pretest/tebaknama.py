import sys

print("")
nama = ["Septi","Bayu","Budi","Tono","Dika","Danu","Anto","Elga","Safi","Antum"]
# print(nama[1])

print("GAME TEBAK NAMA")
print("==============================")
print("")

print("Daftar Nama  : ")
for a in nama :
    print (a)
print("")
print("==============================")

print("Player 1, Masukkan Nama : ")
jawab = str(input())
print("==============================")

if jawab == nama[0] :
    jawaban = jawab
elif jawab == nama[1] :
    jawaban = jawab
elif jawab == nama[2] :
    jawaban = jawab
elif jawab == nama[3] :
    jawaban = jawab
elif jawab == nama[4] :
    jawaban = jawab
elif jawab == nama[5] :
    jawaban = jawab
elif jawab == nama[6] :
    jawaban = jawab
elif jawab == nama[7] :
    jawaban = jawab
elif jawab == nama[8] :
    jawaban = jawab
elif jawab == nama[9] :
    jawaban = jawab
else :
    print("Nama Tidak Terdaftar")
    sys.exit()

print()
print("Player 2, Tebak Nama : ")
tebak = str(input())

if tebak == jawaban :
    print("Selamat Anda Benar")
else :
    print("Coba Lagi")
    print("Kesempataan  : 2")
    print()
    print("==============================")
    print()
    print("Player 2, Tebak Nama : ")
    tebak = str(input())

    if tebak == jawaban :
        print("Selamat Anda Benar")
    else :
        print("Coba Lagi")
        print("Kesempataan  : 1")
        print()
        print("==============================")
        print()
        print("Player 2, Tebak Nama : ")
        tebak = str(input())

        if tebak == jawaban :
            print("Selamat Anda Benar")
        else :
            print("Kesempatan Anda Sudah Habis")



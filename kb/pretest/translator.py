import sys


print("TRANSLATOR")
print("==============================")
print()

print("Input Kata : ", end='')
kata = str(input())

if kata == "Saya" :
    print("Kaji")
elif kata == "Kamu" :
    print("Sia")
elif kata == "Mandi" :
    print("Maneng")
elif kata == "Makan" :
    print("Mangan")
elif kata == "Tidur" :
    print("Tunung")
else :
    print("Kata Tidak Terdaftar")
    sys.exit()

print()

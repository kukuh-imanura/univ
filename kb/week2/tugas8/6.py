operator = ""

while operator != "exit" :
    operator = input("Masukkan Operasi : ")

    if operator == "exit" :
        break

    if operator != "+" and operator != "-" and operator != "*" and operator != "/" :
        print("Operasi tidak di dukung")
        continue

    a = int(input("Masukkan Nilai 1 : "))
    b = int(input("Masukkan Nilai 2 : "))

    if operator == "+" :
        result = a + b
    elif operator == "-" :
        result = a - b
    elif operator == "*" :
        result = a * b
    elif operator == "/" :
        result = a / b
    
    print(f"Hasil : {result}")

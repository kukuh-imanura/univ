cba = 0
num = 8
lim = 3

while cba < lim :
    guess = input("Tebak Angka : ")
    guess = int(guess)

    if guess == num :
        print("Winn")
        break

    cba += 1

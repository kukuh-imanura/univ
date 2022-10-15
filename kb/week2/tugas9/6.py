num = (5, 6, 7, 8, 1)
print(num)

a, b, c, d, e = num
print(e)

_, _, _, a, _ = num
print(a)

a, *b = num
print(a)
print(b)
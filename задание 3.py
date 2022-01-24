run = int(input('введите любое целое, положительное число '))

r = 1
while run > 10:
    d = run % 10
    run //= 10
    if d > r:
        r = d
print(r)
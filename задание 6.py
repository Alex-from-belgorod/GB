a = int(input('Результат первого дня '))
b = int(input('К какому результату стремимся '))

day = 1
if a > b:
    print(day)
while a < b:
    a = a + a/10
    day += 1
print(day)
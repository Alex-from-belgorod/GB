while True:
    s=input ('Введите что нибудь_')
    if s== 'выход':
        print("End programm.")
        break
    
    if len(s)<4:
        print('слишком мало')
        continue
    print('Введеная строка достатоной длинны.')
    
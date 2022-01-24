def x_pow(x, y):
    try:
        res = x ** y
    except TypeError:
        return "ошибка"
    return res
print(x_pow(2, -4))
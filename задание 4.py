import datetime

def convert(n):

    return str(datetime.timedelta(seconds = n))

n = input ('Введите любое число ')
n = int(n)

print (convert(n))
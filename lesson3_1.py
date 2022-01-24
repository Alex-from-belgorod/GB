def div(*args):

    try:
        arg1 = int(input("Input dividend "))
        arg2 = int(input("Input divider "))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Wrong devider! You can't use zero as a devider"

    return res


    if arg2 != 0:
        return arg1 / arg2
    else:
        print("Wrong number! Devider can't be null")



print(f'result  {div()}')
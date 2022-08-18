def divide(a, b):
    try:
        c = a/b
    except ZeroDivisionError:
        print('Invalid!')

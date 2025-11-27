def C():
    print('введите часы:')
    h = int(input())
    print('введите минуты:')
    m = int(input())
    print('введите секунды:')
    b = int(input())
    return h, m, b

def f(h, m, b):
    C = h * 60 * 60 + m * 60 + b
    return C
a, b, c = C()

r = f(a, b, c)
print('количество сек',r)

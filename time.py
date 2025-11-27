print('введите часы')
a= int(input())
print('введите минуты')
b= int(input())
print('введите секунды')
c= int(input())

def f(a,b,c):
    f= a*60*60+b*60+c
    return f
r= f(a,b,c)

print(r)
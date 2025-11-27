print("введите число")
C= float(input())
def f(C):
    f= C%2
    if f==0:
        return ('чет')
    elif f !=0 :
        return ('нечет')

r= f(C)

print(r)
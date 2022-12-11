def greater_between2(a,b):
    if a>b:
        return a
    else :
        return b

def great3(a,b,c):
    bigger=greater_between2(a,b)
    return greater_between2(bigger,c)
a=int(input())
b=int(input())
c=int(input())
print(great3(a,b,c))

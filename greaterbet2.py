def greater_between2(a,b):
    if a>b:
        return a
    else :
        return b
a=int(input("1 no. "))
b=int(input("2 no. "))
bigger=greater_between2(a,b)
print(f"{bigger} is greater")
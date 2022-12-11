def odd_even(l):
    a=[]
    b=[]
    c=[]
    for i in l:
        i=int(i)
        if i%2==0:
            a.append(i)
        else:
            b.append(i)
    c.append(a)
    c.append(b)
    return c

a=input(" enter numbers with space seperated : ").split(" ")
print(odd_even(a))
    
def revlist(l):
    b=[]
    for i in l:
        k=i[::-1]
        b.append(k)
    return b


a=input(" enter strings with space seperated : ").split(" ")
print(revlist(a))

def nooflist(l):
    k=0
    for i in l:
        if type(i)==list:
            k=k+1
    return k
a=[["satish"],5,6,4,["kamlesh","kamlesh"]]
print(nooflist(a))
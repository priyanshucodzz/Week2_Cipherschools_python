a=input(" enter numbers with space seperated : ").split(" ")
b=[]
for i in a:
    i=int(i)
    b.append(i*i)

print(b)
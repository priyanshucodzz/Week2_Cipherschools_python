def comman(l,ls):
    com=[]
    for i in l:
        
        for j in ls:
            
            if i==j:
                com.append(int(j))
    return com


a=input(" enter numbers with space seperated : ").split(" ")
b=input(" enter numbers with space seperated : ").split(" ")
print(comman(a,b))

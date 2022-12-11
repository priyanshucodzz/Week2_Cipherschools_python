
print("*******************************")

for i in range(1,10+1):
    if i%4==0:
        continue
    else:
        print(f"num : {i}")

print("************************")
print("######################")

for i in range(1,10+1):
    if i%4==0:
        break
    else:
        print(f"num : {i}")
print("######################")
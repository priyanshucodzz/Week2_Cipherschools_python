import random


a=random.randint(1,100)
b=1
c=int(input("guess a no. between 1-100 ; "))
game_over=False
while(not game_over):
    if c==a:
        print(f"you won . it takes u {b} fillup to guess")
        game_over=True
    else:
    
        if c>a:
            print("to high ")
        elif c<a:
            print("to low")

    b+=1
    c=int(input("guess again ; "))


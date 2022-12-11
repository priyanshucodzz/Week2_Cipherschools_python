user_info={
    "name": "satish",
    "fav_anime":["one piece","Naruto","Dragon Ball Z","Attack on titan","Demon slayer"],
    "fav_movie":"the dark knight",

}
d=dict.fromkeys(["name","age","height"],"unknown")
# fromkeys is used to create unknown keys of dictionary

print(d)
# we can also use range function in fromkeys
# like 
k=dict.fromkeys(range(1,11),"unknown")
print(k)
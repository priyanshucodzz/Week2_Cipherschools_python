user_info={
    "name": "satish",
    "fav_anime":["one piece","Naruto","Dragon Ball Z","Attack on titan","Demon slayer"],
    "fav_movie":"the dark knight",

}
for i in user_info:
    print(i)
# agar user info ke sath key ya value na lagae to wo default key hi leta hai

# as i say we have keys method and values method avilable 
print(user_info.values())
print(type(user_info.values()))
print(user_info.keys())
print(type(user_info.keys()))


# we can also get values by this method as below
for i in user_info:
    print(user_info[i])
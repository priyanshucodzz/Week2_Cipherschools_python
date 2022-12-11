user_info={
    "name": "satish",
    "fav_anime":["one piece","Naruto","Dragon Ball Z","Attack on titan","Demon slayer"],
    "fav_movie":"the dark knight",

}
# 1.how to add data
user_info["fav_reels"]=["anime","computer science"]
print(user_info)

# 2.pop method to pop a data
k=user_info.pop("fav_movie") 
# it will only give value not key
print(k)
print(user_info)

# 3. popitem method
print(user_info.popitem())
# it will remove key value pair and store a key value pair both




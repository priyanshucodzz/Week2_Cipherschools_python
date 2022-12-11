user_info={
    "name": "satish",
    "fav_anime":["one piece","Naruto","Dragon Ball Z","Attack on titan","Demon slayer"],
    "fav_movie":"the dark knight",

}
print(user_info.items())
# as u can see it convert evey key value pair into tuples

# esse fayda kya???
# ans:- we can acces both keys and values at same time
# example

for i,j in user_info.items():
    print(f"key is {i} and value is {j}")
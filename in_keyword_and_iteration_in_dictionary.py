user_info={
    "name": "satish",
    "fav_anime":["one piece","Naruto","Dragon Ball Z","Attack on titan","Demon slayer"],
    "fav_movie":"the dark knight",

}

# 1. check if key exist
if "name" in user_info:
    print("present")
else:
    print("not present")

# 2. to check values

if "satish" in user_info.value():
    print("present")
else:
    print("not present")


# value method :- it takes all value of dicttionary and make a list
# key method in dictionary :- it takes all keys from dictionary and make a list

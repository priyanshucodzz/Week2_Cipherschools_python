user_info={
    "name": "satish",
    "fav_anime":["one piece","Naruto","Dragon Ball Z","Attack on titan","Demon slayer"],
    "fav_movie":"the dark knight",

}
print(user_info.get("fav_anime"))
print(user_info.get("names"))


if user_info.get("name"):
    print("present")
else:
    print("absent")

# we can also use clear and copy method on dictionaries
# one more thing about get method
print(user_info.get("names","not found"))
# jo , ke bad likha hai uska matlab hai agr names nahi find hua to not found print kra dena

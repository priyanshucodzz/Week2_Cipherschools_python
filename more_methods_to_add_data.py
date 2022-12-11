fruits=["lorem","lorem2"]
# append kewal last mai data ko add karta hai list ke 
# 1. insert method 
fruits.insert(1,"kamlesh")
fruits.insert(200,"kajuuu")
# agar list ke aukaat se jayada ka address daloge to wo last mai store ho jayegi

haweli=["bypass","kaluuuaroad"]
# 2. adding two list
print(fruits+haweli)

# 3.extend method
fruits.extend(haweli)
print(fruits)

# 5.append vs extend
haweli.append(fruits)
print(haweli)
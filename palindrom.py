def is_palindrom(a):
    return a==a[::-1]

a=input()
print(is_palindrom(a))
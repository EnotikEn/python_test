def return_my_value():
    global a
    a = 10
    return a


b = 10
return_my_value()
print(a)
print(a is b)

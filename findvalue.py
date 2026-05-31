def get_key(val):
  
    for key, value in my_dict.items():
        if val == value:
            return key

    return "key doesn't exist"


# Driver Code
my_dict = {"Java": 100, "Python": 112, "C": 11}

print(get_key(100))
print(get_key(11))
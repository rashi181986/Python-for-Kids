# Check the frequency of a value in a dictionary

test_dict = {
    'a': 10,
    'b': 20,
    'c': 10,
    'd': 30,
    'e': 10
}

value = int(input("Enter the value to find frequency: "))

frequency = list(test_dict.values()).count(value)

print("Frequency of", value, "is", frequency)
def list_length(lst):
    # Base case
    if lst == []:
        return 0

    # Recursive case
    return 1 + list_length(lst[1:])

# Example list
my_list = [10, 20, 30, 40, 50]

print("Length of the list:", list_length(my_list))
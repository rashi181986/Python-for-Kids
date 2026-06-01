def find_all_substrings(s):
    substrings = []
    n = len(s)
    
    # Outer loop for the starting index
    for i in range(n):
        # Inner loop for the ending index
        for j in range(i + 1, n + 1):
            # Slice the string from i to j
            substrings.append(s[i:j])
            
    return substrings

# User Input
user_string = input("Enter a string: ")
result = find_all_substrings(user_string)

print(f"All substrings of '{user_string}':")
print(result)
print(f"Total count: {len(result)}")

import random
import string

def generate_password(length=12):
    # Combine uppercase letters, lowercase letters, and digits
    characters = string.ascii_letters + string.digits
    
    # Randomly pick characters from the pool
    password_list = [random.choice(characters) for _ in range(length)]
    
    # Shuffle the list to ensure extra randomness
    random.shuffle(password_list)
    
    # Join the list into a single string
    return "".join(password_list)

# Generate and print a 12-character password
print("Your random password is:", generate_password(12))

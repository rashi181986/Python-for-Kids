class Dog:
    # Class Variable: Shared by all instances
    species = "Canis familiaris"

    def __init__(self, name, breed):
        # Instance Variables: Unique to each instance
        self.name = name
        self.breed = breed

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Species: {self.species}")
        print("-" * 20)

# Creating two dog objects of different breeds
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Bella", "Beagle")

# Displaying their details
print("Dog 1 Details:")
dog1.display_details()

print("Dog 2 Details:")
dog2.display_details()

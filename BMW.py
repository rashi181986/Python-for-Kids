class BMW:
    def info(self):
        print("BMW: The Ultimate Driving Machine.")

    def max_speed(self):
        print("BMW max speed is 240 km/h.")

class Ferrari:
    def info(self):
        print("Ferrari: Symbol of speed and luxury.")

    def max_speed(self):
        print("Ferrari max speed is 340 km/h.")

# Creating objects
car1 = BMW()
car2 = Ferrari()

# Demonstrating Polymorphism
# We can iterate through different objects and call the same methods
for car in (car1, car2):
    car.info()
    car.max_speed()
    print("-" * 15)

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        # Base fare is capacity * 100
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        # Get the base fare from the parent class
        base_amount = super().fare()
        # Add a 10% maintenance charge specifically for buses
        total_amount = base_amount + (0.1 * base_amount)
        return total_amount

# Example Usage:
school_bus = Bus("School Volvo", 12, 50)
print(f"Vehicle Name: {school_bus.name}")
print(f"Total Bus fare is: {school_bus.fare()}")

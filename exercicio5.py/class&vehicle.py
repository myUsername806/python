# ------------------------------
# Assignment 1: Smartphone Class
# ------------------------------

class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
    
    def call(self, number):
        print(f"{self.model} is calling {number} 📞")
    
    def take_photo(self):
        print(f"{self.model} takes a photo 📸")

# Inherited Class
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, cooling_system):
        super().__init__(brand, model, storage)
        self.cooling_system = cooling_system
    
    def play_game(self, game):
        print(f"{self.model} is playing {game} 🎮 with {self.cooling_system} cooling!")

# Test Assignment 1
print("=== Assignment 1: Smartphone Example ===")
phone1 = Smartphone("Apple", "iPhone 15", "256GB")
phone2 = GamingPhone("Asus", "ROG Phone 7", "512GB", "Liquid Cooling")

phone1.call("123-456-7890")
phone1.take_photo()

phone2.call("987-654-3210")
phone2.play_game("PUBG Mobile")

print("\n")

# ------------------------------
# Activity 2: Polymorphism Example
# ------------------------------

class Vehicle:
    def move(self):
        print("This vehicle moves somehow 🚙")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Test Activity 2
print("=== Activity 2: Polymorphism with Vehicles ===")
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()

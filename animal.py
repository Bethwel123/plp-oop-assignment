class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Animal):
    def move(self):
        return f"{self.name} the dog is running happily! 🐕"
    
    def speak(self):
        return f"{self.name} says: Woof! Woof! 🐶"


class Fish(Animal):
    def move(self):
        return f"{self.name} the fish is swimming gracefully! 🐟"
    
    def speak(self):
        return f"{self.name} says: Blub blub... 🐠"


class Bird(Animal):
    def move(self):
        return f"{self.name} the bird is flying high! 🦅"
    
    def speak(self):
        return f"{self.name} says: Tweet tweet! 🐦"


class Snake(Animal):
    def move(self):
        return f"{self.name} the snake is slithering silently! 🐍"
    
    def speak(self):
        return f"{self.name} says: Hisssss... 🐍"


# Demonstration
if __name__ == "__main__":
    print("=== Animal Polymorphism Demo ===")
    
    animals = [
        Dog("Buddy"),
        Fish("Nemo"),
        Bird("Tweety"),
        Snake("Viper")
    ]
    
    for animal in animals:
        print(animal.move())
        print(animal.speak())
        print()  # empty line for spacing
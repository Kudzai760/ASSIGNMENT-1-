class Dog:
    def make_sound(self):
        return "Woof!"

# Define the Cat class
class Cat:
    def make_sound(self):
        return "Meow!"

# Define the process_sound function
def process_sound(sound_object):
    # Call the make_sound method on the passed object
    print(sound_object.make_sound())

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()


process_sound(dog)  # Output: Woof!

process_sound(cat)  # Output: Meow!


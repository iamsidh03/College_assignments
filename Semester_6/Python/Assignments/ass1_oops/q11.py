'''Duck typing is a concept in dynamic typing languages like Python. It means:

“If it looks like a duck, swims like a duck, and quacks like a duck, then it's a duck.”

In Python, this means:

You don’t check what type an object is.

You only care if it has the required method or behavior.

So if an object has a speak() method, we don’t care what class it belongs to — we just call speak().'''

# Duck typing in action

def describe(obj):
    # This function accepts any object with a speak() method
    print("Description:")
    obj.speak()  # We don't care what type 'obj' is — only that it has speak()

class Dog:
    def speak(self):
        print("Woof! I am a Dog.")

class Robot:
    def speak(self):
        print("Beep boop! I am a Robot.")

# Create instances of Dog and Robot
dog = Dog()
robot = Robot()

# Pass them to describe function
describe(dog)
describe(robot)

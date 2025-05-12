# # 🦆 What is Duck Typing in Python?
# Duck typing is a concept in dynamic typing where the type or class of an object is less important than the methods it defines.

# The saying goes:
# “If it walks like a duck and quacks like a duck, it’s a duck.”

'''
 Problem Requirements:
Define a function describe(obj) that calls obj.speak().

Create two classes: Dog and Robot, both implementing a speak() method.

Pass both to describe() without checking their types.

'''
class Dog:
    def speak(self):
        print("dog speaking whao whao")

class robot:
    def speak(self):
        print("robot speak hey..")

def describe(obj):
    obj.speak()        

d=Dog()
r=robot()
describe(d)
describe(r)
'''
The function describe(obj) does not check if obj is an instance of Dog or Robot.

It just assumes obj has a speak() method.

Both Dog and Robot satisfy this requirement, so it works without error.'''


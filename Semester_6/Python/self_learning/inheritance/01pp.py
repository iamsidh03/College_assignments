# class Animal: #Single Inheritance
#     def speak(self):
#         print('Animal Spreaks')
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")

# d=Dog()
# d.speak() #Inherited method
# d.bark() #Dog's own method

# 2. Using super()
# super() is used to call methods (especially the constructor) from the parent class inside the child class.
class Animal:
    def __init__(self,name):
        self.name=name

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
        print("Dog initialized")
d=Dog('Hbhdf','labrador')

print(d.breed)
print(d.name)
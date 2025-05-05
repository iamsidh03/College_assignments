'''
🧪 Exercise: Create a Car Class
🔧 You need to:

Define a class called Car.

Add a constructor __init__() that takes 3 arguments: brand, model, and year.

Store those values in instance variables.

Create a method display_info() that prints the car's details.

Create two different objects of the class and call the method for both.

✅ Example Output:
yaml
Copy
Edit
Brand: Toyota, Model: Corolla, Year: 2020
Brand: Honda, Model: Civic, Year: 2022
'''
class car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

    def display(self):
        print(f'Brand: {self.brand}, Model: {self.model}, Year: {self.year}')

    def is_old(self):
        current_yr=2025
        current_age=current_yr - self.year
        if current_age >5:
            print(f"{self.model} is older then five year and current age of car is {current_age} ")

        else:
            print(f'{self.model}  is not old ')
car1=car('Toyota','Corolla',2000)
car2=car('Honda','Civic',2022)
car1.display()
car2.display()
car1.is_old()

'''
Add a method is_old() that:

Checks if the car is older than 5 years.

Prints "Old Car" or "New Car".
'''
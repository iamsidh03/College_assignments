'''
Problem 1: Employee Class with Bonus
Task:
Create a class Employee with attributes name, salary, and bonus.

If the bonus is not provided, default it to 5000.

Add a method total_salary() that returns the total salary (salary + bonus).

Create at least 2 objects and test them.
'''

class Employee:
    def __init__(self,name,salary,bonus=5000):
        self.name=name
        self.salary=salary
        self.bonus=bonus
    def total_salary(self):
        return self.salary+self.bonus
    
e1=Employee('raj',400000000,300000)
e2=Employee('ravi',400,30)
print(e1.total_salary())
print(e2.total_salary())
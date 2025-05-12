# Example 1: Private Attributes and Manual Get/Set
class Student:
    def __init__(self,name,grade):
        self.__name=name
        self.__grade=grade
    def get_grade(self):
        return self.__grade
    
    def set_grade(self,grade):
        if 0<=grade<=100:
            self.__grade=grade
        else:
            print("invalid grade")

s=Student('Raj',30)
# print(s.get_grade())
# s.set_grade(10)
# print(s.get_grade())

# ✅ Using @property in Python (The Clean Way to Use Encapsulation)
class Student:
    def __init__(self,name,grade):
        self.__name=name
        self.__grade=grade
    
    @property
    def grade(self):
        return self.__grade
    @grade.setter
    def grade(self,value):
        if 0<=value<=100:
            self.__grade=value
        else:
            print('grade must br between 0 and 100')

s=Student('Alice',88)
print(s.name) #can't  acces directly as it is private attribute
print(s.grade)
s.grade=95 #Allowed

s.grade=120 #not allowed
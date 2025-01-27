'''
class Bulletecho:
    def __init__(self,name,level,weapon):
        self.name=name
        self.level=level
        self.weapon=weapon
    def highlevel(self):
        if self.level>75:
            print(f'{self.name} is a high level character')
        else:
            print(f'{self.name} is a high level character')

char1=Bulletecho('Bastion',87,'Machine Gun')
char2=Bulletecho('Firefly',76,'Sniper')
char3=Bulletecho('Levi',37,'assault rifle')
class MoreProps(Bulletecho):
    def __init__(self,name,level,weapon,health,armour):
        super().__init__(name,level,weapon)
        self.health=health
        self.armour=armour
        
# print(char1.level)
# print(char2.level)
# print(char1.weapon)
# print(char2.weapon)
char4=MoreProps('FireFlly',76,'sniper',100,100)
print(char4.health)
char1.highlevel()

'''

'''
#question2 
class Mobile:
    def __init__(self,brand,battery,memory):
        self.brand=brand
        self.battery=battery
        self.memory=memory
    def calling(self):
        if self.battery>25:
            print("calling is possible")
        else:
            print("Not possible")
            
    def texting(self):
        if self.battery>15:
            print("texting is possible")
        else:
            print("Not possible")
    def gaming(self):
        if self.battery>40 and self.memory>64:
            print("Gaming is possible")
        else:
            print("Gaming Not possible")
sam=Mobile('samsung',20,32)




'''










  
  
  
  
  
  
'''Question4'''
  # create a class called car 
# attributes: brand,milage pretrol/diesel
# method: owning_cretria : if brand is audi, I'll buy
# milage_critria: if milage>10000, i will go to ITER

# inherit car is another class call newCar
# attributes:electric
# methods: if color=blue or black, then buy
# Q) will I drive a grey car
class Car:
    def __init__(self,brand,milage,petrol,diesel):
            self.brand=brand    
            self.milage=milage
            self.petrol=petrol
            self.diesel=diesel
    def owing_cretria(self):
        if self.brand=='audi':
            print('I\'ll buy')

    def milage_critria(self):
        if self.milage==10000:
            print('I\'ll go to ITER')

class NewCar(Car):
    def __init__(self,brand,milage,petrol,diesel,electric,color):
        super().__init__(brand,milage,petrol,diesel)
        self.electric=electric
        self.color=color
    def color():
        if self.color=='black' or self.color=='blue':
            print('I will buy')
        
char=NewCar('audi',20000,'Y','No','No','black')
print(char.color)
print(char.brand)
char.owing_cretria()
























# create a class Grandparents having 3 atributes a,b,c
# and two method GP1,GP2
# inherit class grandparents in class parents having 4 attributes 
# a,b,d,e and 3 methods GP1,GP2,P1
# inherit class parents in class child having 5 attributes 
# a,b,d,f,g and 4 method GP1,GP2,P1,C1

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # Grandparents class with 3 attributes and 2 methods
class Grandparents:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def GP1(self):
        print("Grandparents method GP1 called")

    def GP2(self):
        print("Grandparents method GP2 called")


# Parents class inherits from Grandparents, has 4 attributes and 3 methods
class Parents(Grandparents):
    def __init__(self, a, b, c, d, e):
        super().__init__(a, b, c)  # Initialize Grandparents' attributes
        self.d = d
        self.e = e

    def GP1(self):
        print("Parents method GP1 called")

    def GP2(self):
        print("Parents method GP2 called")

    def P1(self):
        print("Parents method P1 called")


# Child class inherits from Parents, has 5 attributes and 4 methods
class Child(Parents):
    def __init__(self, a, b, c, d, e, f, g):
        super().__init__(a, b, c, d, e)  # Initialize Parents' attributes
        self.f = f
        self.g = g

    def GP1(self):
        print("Child method GP1 called")

    def GP2(self):
        print("Child method GP2 called")

    def P1(self):
        print("Child method P1 called")

    def C1(self):
        print("Child method C1 called")


# Example of usage:
child = Child(a=1, b=2, c=3, d=4, e=5, f=6, g=7)
child.GP1()  # Calls Child's GP1
child.GP2()  # Calls Child's GP2
child.P1()   # Calls Child's P1
child.C1()   # Calls Child's C1

        
        
    

# class Item:
#     pass
# Item.name="Phone"
# Item.ram="4GB"
# Item.brand="OnePlues"
# print(Item.name)
# print(Item.ram)
# print(Item.brand)

'''
class->(keywords)Blueprint of creating object
Item->(class Name) by convention class name is upper case
pass->(keyword) just a placeholder Name it means 'do nothing' all the class to be synatically correct
without 'pass' class in the above case  would be empty and  couse error

aditional points
we can use 'pass' in loop, functions or any where when we want to not execute the code
examples:
if x > 5:
    pass  # Do nothing for now
else:
    print("x is less than or equal to 5")

    
what is attribues in python?
It is the variable associated with class an object.
two types:
1) class Attributes
2) instance Attributes

In the above examples of class attributes are 'name','ram','brand'

Items.name-> means name attributes or variable belong to class items



'''

# class Items:
#     def cal_prices(self,x,y):
#         return x*y
    

#  the below lines Gives error because object is not created

#print(cal_prices(40,30)) this will give you error you have to specify that 'cal_price' belog to which class using '.' operator

#print(Items.cal_prices(40,30)) also gives error

# Items.price=40
# Items.quantity=6
# print(Items.cal_prices(Items.price,Items.quantity)) 

#so first creats an object
'''
What is objects
Instance of class that contains data(attributes) and method(behaviour) defined by a class

'''

# item1=Items()
# item1.price=400
# item1.quantity=40
# print(item1.cal_prices(item1.price,item1.quantity))

# print(item1.cal_prices(40,30))

# class Items:
#     def __init__(self,name):
#         print(f'The instance created for {name}')
    
# Item1=Items("Phones")
# Item2=Items("Car")

'''
__init__ -> It is the special method in python also known as constructor that is called automatically when when new object(instance) is created
def -> Define a function/method
self -> reference to the current instance


'''

'''
"Write a Python class Items that represents a product with a name, price, and quantity. 
The class should have a method cal_val() that calculates and returns the total value of the item (price × quantity).
 Create an instance of the class with sample values and print the total value."
'''
'''
class Items:
    #def __init__(self,name,price,quantity=0): #if you not pass any argument to quantity the by default it take as 0
    def __init__(self,name :str,price :float,quantity=0): # define datatype also name takes string only and price take float only
       
        assert price>=0,f"{price} must be greater then zero"
        #if price is less then 0 then Assertion Error occur
        self.name=name
        self.price=price
        self.quantity=quantity
    
    def cal_val(self):
        return self.price*self.quantity

    
item1=Items("phone",10000,20)
#item1=Items("phone",'10000',20)
#if you pass integer as string 
print(item1.cal_val())

'''
# Now we are leaning class Attributes

class Items:
      pay_rate=0.8#pay rate after 20% discount
      all=[]
      def __init__(self,name :str,price :float,quantity=0): # define datatype also name takes string only and price take float only
       
        assert price>=0,f"{price} must be greater then zero"
        #if price is less then 0 then Assertion Error occur
        self.name=name
        self.price=price
        self.quantity=quantity

        Items.all.append(self)# create all the instances of Items
    
      def cal_val(self):
          return self.price*self.quantity
      def apply_discount(self):
          self.price=self.price*self.pay_rate
      def __repr__(self):
          return f"Items('{self.name}',{self.price},{self.quantity})"

    
item1=Items("phone",10000,20)
item1.apply_discount()
print(item1.price)

item2=Items("laptop",10000,2)
item2.pay_rate=0.7
item2.apply_discount()

print(item2.price)
item3=Items("Cable",20,5)
item4=Items("Mouse",50,5)
item5=Items("Keywords",75,5)

#print(Items.all)
for instances in Items.all:
    print(f"{instances.name},{instances.price},{instances.quantity}")


#https://www.youtube.com/watch?v=Ej_02ICOIgs&t=1052s



'''
Problem: Inventory and Product Classes
You're building a mini system for managing a store's inventory.

✅ Requirements:
Class Product:

Attributes: name, price, quantity

Method total_value() → returns total value of this product (price * quantity)

Class Inventory:

Attribute: products (a list of Product objects)

Method add_product(product) → adds a Product object to the inventory

Method show_inventory() → prints name, quantity, and total value of each product

Method inventory_value() → returns total value of all products

Add a method in Inventory:
remove_product(product_name) that removes a product by its name if it exists.
'''
class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def total_value(self):
        return  self.price*self.quantity
    
class Inventory:
    def __init__(self):
        self.product=[]
    def add_product(self,product):
        self.product.append(product)
    def show_inventory(self):
        for i,p in enumerate(self.product):
           print(f'product number {i+1} name: {p.name}, price:{p.price} Quantity: {p.quantity}, Total_value: ${p.total_value()}')
    def remove_product(self, prodToRemove):
        for p in self.product:
            if p.name == prodToRemove:
                self.product.remove(p)
                print(f"{prodToRemove} removed from inventory.")
                return
        print(f"{prodToRemove} not found in inventory.")
 

    def inventory_value(self):
        tsum = 0
        for p in self.product:
            tsum += p.total_value()
        return tsum

    
prod1=Product('mobile',2000,10)
prod2=Product('laptop_cover',20,10)
print(f'total value: {prod1.total_value()}')
inv1=Inventory()
inv1.add_product(prod1)
inv1.add_product(prod2)
inv1.show_inventory()
inv1.remove_product('mobile')
print(f' Total inventory value is {inv1.inventory_value()}')




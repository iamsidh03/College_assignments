class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def __add__(self,other):
        new_real=self.real+other.real
        new_imag=self.imag+self.imag
        return Complex(new_real,new_imag)
    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1=Complex(3,4)
c2=Complex(30,20)
result=c1+c2
print('sum: ',result)
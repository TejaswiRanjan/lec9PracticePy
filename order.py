# Create a class called Order which stores item & its price

# Use Dunder function __gt__() to convey that 

# Order 1> order > if price of order 1> price of order2.

class Order:

    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,odr2):
        return self.price > odr2.price
    
odr1 = Order("Cococola" , 40)
odr2 = Order("String" , 20)

print(odr1 > odr2)
# this imports the CashRegister and Product classes so they can be used here.
# Note that the cash_register.py and person.py files must be in the same folder
# as this file.
from cash_register import CashRegister
from product import Product

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def __str__(self):
        return ("This person's name is " + self.first_name + " " +
                self.last_name + ". They are " + str(self.age) + " years old.")

    def birthday(self):
        self.age = self.age + 1

# Customer is a subclass of Person
class Customer(Person):
    def __init__(self, total_money, shopping_list, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.total_money = total_money
        self.shopping_list = shopping_list
        self.cart = []
        self.cart_size = 0
    
    def select(self, prod):
        self.cart_size = self.cart_size + 1
        self.cart.append(prod)
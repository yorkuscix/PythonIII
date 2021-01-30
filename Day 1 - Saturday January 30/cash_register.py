class CashRegister:
    def __init__(self, loonies, toonies, fives):
        self.loonies = loonies
        self.toonies = toonies
        self.fives = fives
    
    def get_total(self):
        return self.loonies + 2*self.toonies + 5*self.fives

'''
This is a block comment. None of these lines run at all!

To create a CashRegister, run in the shell:

cr1 = CashRegister(1, 5, 2)

Remember that we are just creating a variable of type "CashRegister"
this one is called cr1, but we could call it anything we want.

This cash register is initialized with 1 loonie, 5 toonies, and 2 fives.

To get the total value in a cash register, run in the shell:

cr1.get_total()
'''
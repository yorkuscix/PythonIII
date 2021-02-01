class CashRegister:
    def __init__(self, loonies, toonies, fives):
        self.loonies = loonies
        self.toonies = toonies
        self.fives = fives
    
    def get_total(self):
        return self.loonies + 2*self.toonies + 5*self.fives
    
    def add(self, count: int, denomination: str):
        if denomination == "loonies":
            self.loonies = self.loonies + count
        if denomination == "toonies":
            self.toonies = self.toonies + count
        if denomination == "fives":
            self.fives = self.fives + count
            
    # TODO: don't allow removing more of a denomination than exist in the cash register
    def remove(self, count: int, denomination: str):
        if denomination == "loonies":
            self.loonies = self.loonies - count
        if denomination == "toonies":
            self.toonies = self.toonies - count
        if denomination == "fives":
            self.fives = self.fives - count
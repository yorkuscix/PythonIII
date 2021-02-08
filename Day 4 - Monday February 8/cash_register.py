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
            
    def remove(self, count: int, denomination: str):
        if denomination == "loonies":
            if self.loonies >= count:
                self.loonies = self.loonies - count
            else:
                return "Not enough loonies. This cash register only has " + str(self.loonies)
        if denomination == "toonies":
            if self.toonies >= count:
                self.toonies = self.toonies - count
            else:
                return "Not enough toonies. This cash register only has " + str(self.toonies)
        if denomination == "fives":
            if self.fives >= count:
                self.fives = self.fives - count
            else:
                return "Not enough fives. This cash register only has " + self.fives
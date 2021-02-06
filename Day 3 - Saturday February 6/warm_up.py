class Car:
    def __init__(self, licence_plate, num_of_wheels, colour):
        self.licence_plate = licence_plate
        self.num_of_wheels = num_of_wheels
        self.colour = colour        

    def __lt__(self, other):
        return self.licence_plate < other.licence_plate
    
    def __gt__(self, other):
        return self.licence_plate > other.licence_plate
    
    def __eq__(self, other):
        return self.licence_plate == other.licence_plate
    
    def __str__(self):
        return ("This " + self.colour + " car has " + str(self.num_of_wheels) +
                " wheels. Its licence plate is " + self.licence_plate + ".")
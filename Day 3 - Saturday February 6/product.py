class Product:
    def __init__(self, name, price, section, id_num):
        self.name = name
        self.price = price
        self.section = section
        self.id_num = id_num
        self.sort_field = "price"

    def __lt__(self, other):
        if self.sort_field == "name":
            return self.name < other.name
        if self.sort_field == "price":
            return self.price < other.price
    
    def __gt__(self, other):
        if self.sort_field == "name":
            return self.name > other.name
        if self.sort_field == "price":
            return self.price > other.price
    
    def __eq__(self, other):
        return self.id_num == other.id_num
    
    def __str__(self):
        return ("This is a " + self.name + ". It can be found in the " +
                self.section + " section. It costs $" + str(self.price))

'''
Try creating a list of products and sorting them by different properties.
Create a function to change the sort_field property (hint: refer to the add function from last week)

To create a list of products try:
shopping_list = [Product("Apple", 1.0, "Produce", 111), Product("Can Opener", 4.0, "Appliances", 543), Product("Banana", 0.5, "Produce", 999)]

Then sort with,
shopping_list.sort()

Then print out the results with,
for item in shopping_list:
    print(item)
'''
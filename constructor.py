# Creating a class

class car():

    def __init__(self, modelname, yearm, price):  # Creating constructor

        # Specifying variables or instances

        self.modelname = modelname
        self.yearm = yearm
        self.price = price

    def price_inc(self):  # Creating function inside class
        self.price = int(self.price * 1.15)

# Passing parameter to the objects
honda = car('City', 2007, 100000)
tata = car('Bolt', 2009, 500000)

honda.cc = 1500  # Creating & assigning new variable to the existing object without passing inside parameter

print(honda.cc)  # Printing above type of variable

print(tata.modelname)  # Printing single variable term

print(honda.__dict__)  # Printing all the parameters of an objects using dictionary functions

print(honda.price)  # Price before using increment function

honda.price_inc()  # Applying increment function

print(honda.price)  # Price after applying increment function

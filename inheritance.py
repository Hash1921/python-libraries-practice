# Creating a class

class car():

    def __init__(self, modelname, yearm, price):  # Creating constructor

        # Specifying variables or instances

        self.modelname = modelname
        self.yearm = yearm
        self.price = price

    def price_inc(self):  # Creating function inside class
        self.price = int(self.price * 1.15)

class SuperCar(car):
   pass

# Passing parameter to the objects
honda = SuperCar('City', 2007, 100000)
tata = car('Bolt', 2009, 500000)

honda.cc = 1500  # Creating & assigning new variable to the existing object without passing inside parameter
print(help(honda))
print(honda.yearm)
honda.price_inc()
print(honda.price)




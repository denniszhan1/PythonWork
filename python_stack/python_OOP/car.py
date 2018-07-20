class car(object):
    def __init__(self,price,speed,fuel,mileage):
        self.speed=speed
        self.fuel=fuel
        self.mileage=mileage
        self.price=price
        if price>10000:
            self.tax=.15
        else:
            self.tax=.12
        self.display_all()
    
    def display_all(self):
        print "Price:"+ str(self.price)
        print "Speed:"+ str(self.speed) + "mph"
        print "Fuel:"+ str(self.fuel)
        print "Mileage:"+ str(self.mileage) + "mph"
        print "Tax:"+ str(self.tax)

car1 = car(2000, 35, 'Full', 15)
car2 = car(2000, 5, 'Not Full', 105)
car3 = car(2000, 15, 'Kind of Full', 95)
car4 = car(2000, 25, 'Full', 25)
car5 = car(2000, 45, 'Empty', 25)
car6 = car(20000000, 35, 'Empty', 15)
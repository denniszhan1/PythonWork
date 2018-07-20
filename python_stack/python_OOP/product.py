class product(object):
    def __init__(self, price, name, weight, brand, status):
        self.price=price
        self.name=name
        self.weight=weight
        self.brand=brand
        self.status= "For Sale!"

    def sell(self):
        self.status="Sold"
        return self
    
    def add_tax(self,tax):
        self.price= self.price-(self.price*tax)
        return self

    def Return(self, reason,box):
        if reason=="defective":
            self.status=reason
            self.price=0
        if box=="open":
            self.status="Used"
            self.price=self.price-(self.price*.2)
        elif box=="closed":
            self.status= "For Sale!"
        return self
    
    def display_info(self):
        print "Product: %s" %(self.name)
        print "Price: $%s" %(self.price)
        print "Brand: %s" %(self.brand)
        print "Weight: %s lbs" %(self.weight)
        print "Status: %s" %(self.status)

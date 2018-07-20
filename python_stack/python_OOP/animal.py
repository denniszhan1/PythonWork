class Animal(object):
    def __init__(self,name,health):
        self.name=name
        self.health=health
    def walk(self):
        self.health-=1
        return self
    def run(self):
        self.health-=5
        return self
    def display_health(self):
        print "Health=%s" %(self.health)

class Dog(Animal):
    def __init__(self,name):
        super(Dog,self).__init__(self,name)
        self.health=150
    def pet(self):
        self.health+=5
        return self

class Dragon(Animal):
    def __init__(self,name):
        super(Dragon,self).__init__(self,name)
        self.health=170
    def fly(self):
        self.health-=10
        return self
    def display_health(self):
        super(Dragon,self).display_health()
        print "I am a dragon!"

animal1 = Animal("Monty the cat", 100)
animal1.display_health()
animal1.walk()
animal1.run()
animal1.display_health()

dog1 = Dog("Fido")
dog1.display_health()
dog1.walk()
dog1.run()
dog1.pet()
dog1.display_health()

dragon1 = Dragon("Toothless")
dragon1.display_health()
dragon1.walk()
dragon1.run()
dragon1.fly()
dragon1.display_health()
#****************Inheritance**************************

# when one class (child / derived) derives the properties and method of another class (parent / base) class
# when we inherite one class to another class we can use its properties in inherited class as in below example
# syntex:  class class_name:
#                 body of class

#          class new_class_name(class_name):
#                 class_body


class car:
    @staticmethod
    def start():
        print("car started")


    @staticmethod
    def stop():
        print(" car stoped.")

class toyota_car(car): # we created new class "toyouta_car" and inherited parent class tht is "car"  now we can access all properties, function or attributes of "car" class from "toyota_car" class
    def __init__(self, name):
        self.name = name

car1 = toyota_car("fortuner") # here we passed name of car in child class
car2 = toyota_car("prado")

print(car.start()) # here we accessed the function of parent class from child class. 


# ********types of inheritance***************8
#*************Single inheritance******************

# in single inhehritance class there is only one parent class and only one child class
# as we did example above that is the example of dingle inheritance because there is only one parent class "car" and only one child class "toyota_car"

class Car: # parant class
    name = "prado"

class New_car(Car):  # child class and inherited parent class "Car"
    model = "2022"

carr1 = New_car()   # created object of child class
print(carr1.name)   # her we printed name of car form child class but is in parent class



#*******************Multi level inheritance****************

# in multi level inheritance one parent class say "class1" is inherited to child class sya 'class2' and then this child class is inherited to one more clas say "class3"
# now this "class2" is child of "class1" and the parent of "class3" and this "class3" inherited to next class say "class4"
# now 'class4" is child of class3 and class3 is parent of class4 and class 3 is child of class2.  and so on it goes to multi level

# example:
class Vehicle:    #parent class
    def start(self):
        print("Starting vehicle...")

class Car(Vehicle): #child class inherites parent(Vehicle) class. and also is the parent of next class(ElectricCar)
    def drive(self):
        print("Driving car...")

class ElectricCar(Car):  # child class of upper class(Car)
    def charge(self):
        print("Charging electric car...")

# Usage
tesla = ElectricCar()  # created object for ElectricCar class
tesla.start()   #called the function of first parent(Vehicle) class from third child(ElectricCar) class
tesla.drive()   #called the function of second parent(Car) class from third child(ElectricCar) class
tesla.charge()  # called the function of third child(ElectricCar) by itself object




#**********************Multiple Inheritance****************************

#Multiple inheritance means that one child class can use the properties of more then one parent class.
#  means say there are 4 classes, "class1"  "class2" "class3" "class4",   class4 inherites to all 3 classes and can uses the properties of these 3 classes example below

class Phone:  # parend class
    def call(self):
        print("Making a phone call...")

class Camera:  # parend class
    def take_photo(self):
        print("Taking a photo...")

class Whatsappp:   # parend class
    def send_message(self):
        print("Sending a Message...")

class SmartPhone(Phone, Camera, Whatsappp):  # child class inherites to 3 classes  Phone, Camera, Whatsappp    and we can access all properties of all three parent classes from one child class
    def browse(self):
        print("Browsing the internet...")

# Usage
device = SmartPhone()   # created object for child class
device.call()  # called the function of parent class"phone" from child class
device.take_photo()   # called the function of parent class "Camera" from child class
device.send_message()  #called the function of parent  class "Whatsapp" from child class
device.browse()    # called the function of child class by itself object

     #  and also it can goes to mulple classes


# we can inherite a multiple inherited class to other one class as multilevel inheritance and so on

class Phone:   # parent class
    def call(self):
        print("Making a phone call...")

class Camera:   # parent class
    def take_photo(self):
        print("Taking a photo...")

class SmartPhone(Phone, Camera):   # child class inherites to parent class (Phone, Camera)
    def browse(self):
        print("Browsing the internet...")

class SmartWatch(SmartPhone):   # child class inherites parent class Smartphone that is the child class of upper classes
    def track_fitness(self):
        print("Tracking fitness activity...")

# Usage
device = SmartWatch()
device.call()         # Inherited from Phone
device.take_photo()   # Inherited from Camera
device.browse()       # Inherited from SmartPhone
device.track_fitness()# Defined in SmartWatch




#**********************Super Method IN classes*************************
# super method is used to access methods of the parent class.

# The super() method in Python is used to call methods or constructors from a parent class inside a child class.
# It’s especially useful when:
# You want to extend (not override) the parent’s behavior.
# You’re working with multiple inheritance and want Python to handle method resolution automatically.

# Syntax:

# super().method_name()

class Device:  #parent class
    def __init__(self, brand):
        self.brand = brand
        print(f"Device brand: {brand}")

class SmartPhone(Device):  # child class
    def __init__(self, brand, model):
        super().__init__(brand)  # Call parent constructor for brand name
        self.model = model
        print(f"SmartPhone model: {model}")

# Usage
phone = SmartPhone("Samsung", "Galaxy S24") # called child class and passed brand name and model , brand name from constructor calling of  parent class in child class

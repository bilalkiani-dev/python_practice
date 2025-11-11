#***************practice*******************

#Define a Circle class to create a circle with radius r using the constructor. 
# Define an Area( method of the class which calculates the area of the circle. 
# Define a perimeter() method of the class which allow you to calculate the perimeter of the cirlcle.)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return 3.14159*self.radius**2

    def Perimeter(self):
        return 2*3.14159*self.radius
    
circle1 = Circle(5)
print(circle1.Area())
print(circle1.Perimeter())



# Define a Employee class with attributes role, department & salary.
#  this class also has a show details method.
#  Create an Engineer class that inherits properties from Employee & has additional attributes: name and age.

class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print("Employee role is: ", self.role, "\nDepartment is: ", self.department, "\nSalary is RS: ", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", 70000)

    def show(self):
                print("Employee name is: ",self.name, "Age is: ",self.age, "Role is: ", self.role, "\nDepartment is: ", self.department, "\nSalary is RS: ", self.salary)

egr1 = Engineer("Bilal Kiani", 22)
egr1.show()



# Create a class order which so=tores item & its price.  
# Use Dundner function __gt__() to convey that: 
#  ordere1>order2 if price of order1> price of order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    def showDetail(self):
        print("Item name is : ", self.item, "and it's price is Rs: ", self.price)
    def __gt__(ordr1, ordr2):
         return ordr1.price > ordr2.price

ordr1 = Order("Piza", 1599)
ordr1.showDetail()
ordr2 = Order("Chips", 23500)
ordr2.showDetail()
print(ordr1>ordr2)
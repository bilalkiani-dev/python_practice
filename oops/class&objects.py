# ********************************Classes & Objects*********************************

#class is the blue print for creating object:

# syntex for creating class:   class Classname:
#                                    class body


# syntex for class object:     Classname()

class Student:
    name = "Bilal Kiani"
    rollno = 103
    cgpa = 3.21

studentinfo = Student()
print(studentinfo.name, studentinfo.cgpa, studentinfo.rollno)


#**************Constructor**************

#constructor is basically  __init-- function,
# All classes have a function called __init__(), which is always exicuted when the class is being initiated. this function automatically exicutes at the time of object creation

class Student1:
    def __init__(self):   #this function wil lbe created automatically and automatically exicutes when object is created.
        print("Adding new student: ")
        # now the parameter in init function "self" is basically pointing to itself class object,   this "self"  and the object of teh same class are the ssame things we can check below;
        print(self)   # this will print object location 
Student1()  # here we just created an object of the class but the function __init__() in that class also exicuted without calling

#we can pass different parameters in  init function, but the self parameters is always the first prametr,

class Student3:
    def __init__(self, name, rollno, cgpa):
        # the self parameter is a referance to the current instance of the class, and is used to access variables that belongs to the class.
        # this self parameter in init function is default parameter, if didnt give this parameter then python wil automatically create it, whe can access values by self without writing as parameter
        self.fullname = name
        self.rolno = rollno
        self.cgpaa = cgpa
s3 = Student3("Bilal Kiani", 103, 3.21)
print(s3.fullname, s3.rolno, s3.cgpaa)
s4 = Student3("Afan", 68, 3.00)
print(s4.fullname, s4.rolno, s4.cgpaa)

# ****Class and instance (objects) attributes:
#class attributes means the common features that are in class and the object attributes means the features that are different for each object example below:

class Car_features:   #here we created a class for the car features that will be common for each car i will create
    color = "blue"
    auto_doors = True

    def __init__(self, cname, cengine):
        self.carname = cname
        self.carengine = cengine


# here i created some instances   objects that are different for each car but the each car have the common features that are the features of class;
car1 = Car_features("buggati", "5000cc")
car2 = Car_features("prado", "4000cc")
car3 = Car_features("civic", "2000cc")
car4 = Car_features("nissan gtr", "3000cc")


# here printed all feature that these cars have,  common from class and the different from object features
print(car1.carname, car1.color, car1.auto_doors, car1.carengine)
print(car2.carname, car2.color, car2.auto_doors, car2.carengine)
print(car3.carname, car3.color, car3.auto_doors, car3.carengine)
print(car4.carname, car4.color, car4.auto_doors, car4.carengine)


# Methods in class:
  #  basically class is te collection of attributes and Methods, methods are the functions that we can perform in class. like

class Car_info:
    color = "blue"
    doors = "auto"

    def __init__(self, cname, cengine):
        self.carname = cname
        self.carengine = cengine
    
    def welcome(self):   #method
        print("\n, wellcome car: ", self.carname)

    def driving(self,drive):   #method
        print(drive)

carr1 = Car_info("Buggati", "5000cc")
carr2 = Car_info("farrari", "4000cc")

print(carr1.carname, carr1.carengine, carr1.color, carr1.doors, carr1.welcome(), carr1.driving("Auto driving"))
print(carr2.carname, carr2.carengine, carr2.color, carr2.doors, carr2.welcome(), carr2.driving("Menual Driving"))



#*********delete object or attribute in class:
# we use del keyword to delete object or attribute like from above example we wana delete the whole object "car1" and from object only name attribute as below
del carr1  # the object carr1 is deleted now , now if we try to access this, this will give error
del carr2.carname    # by this the attribute car name is deleted now if we try to access car name it will give error


#    practice in new file "practice_class&objects.py"



#******** static methods decorator***************

# if we try to write any function in class without passing "self" parameter it will give error, but if we dont wana give self parameter then we make this function static as below
# static method are the methods that don't use self parameter (works at clss level)
# for making the function static we use a decorator  "@staticmethod"
#decorator is basically allows us to wrap another function in order to extend the behaviour of the wrapped function, wihtout permanently modifying it.

class hello():
    @staticmethod
    def show():
        print("Hellow Bilal!") #normally when we try to call this function this will give error but we use decorator on function nwo it will work perfectly
    show()    # se can call this function only at class level


# ***********************Class method decorator**************************

# A class method is bound to teh class & receives the class as an implicit first argument.
#Note:  static method cannot access or modify class stae and generally for utility.
# static memthod we use when we dont need to use class attributes or instance attributes in that function like

class Hy():
    @staticmethod
    def hyy():  # her in this function we didnt use any class attribute. we made it static. 
        print("Hy bilal!")

# why we use cass method we understand through example below:

class Person():
    name = "Bilal Kiani"  # we created a class of a person and entered name of that person as attribute

    def changeNamme(self, name): # we created a function to change the name
        self.name = name
p1 = Person()   # her we created object for person class
p1.changeNamme("Afan")  # we changed teh name "Bilal Kiani" to "Afan" by calling function and passed name as an argument
print(p1.name)  # we print the name of person p1, this will print new name "Afan"
print(Person.name)  # but here we tried to print name form class name this will print old name "Bilal Kiani", it means that still name not changed in class, this nanme chhanged only as function attribute as creating new name attributte in function

#but we have to changne the name in the whole class,  for this there are different ways but bu class method decorter we do like

class Personn():
    Name = "Saood"

    @classmethod   #class method decorator
    def changeNamee(cls, Name):   # here cls is not now self , its basically now pointing to the class, nme can be any thing liek i write "cls"
        cls.Name=Name

p2 = Personn()
p2.changeNamee("Junaid")  #changed the name
print(p2.Name)  #calling through object
print(Personn.Name)  #calling through class name,  now both wayss work same as cnanges teh name in whole class now


# now here is a little confusion that we discussed three types of methods like
#1). static method,   2). class method,   3). instance method

#instance method: contains the first argument "self" that is an object,   class method: contains the first argument "cls" as class, and the static method: does not changes the attributes of the class or instance they dont contains necessary argument liek self or cls




#*****************Property memthod decorator********************
#understand usage by example:

class student: 
    def __init__(self, math, phy, bio):
        self.math = math
        self.phy = phy
        self.bio = bio
    def calculate_percentage(self,):
        self.percentage = str((self.math+self.phy+self.bio)/3) + "%"

stu1 = student(67, 43, 32) # entered marks of subject
stu1.calculate_percentage() # we called calculate percentage funtion
print(stu1.percentage) #this will print percentage of subjects mamrks

# now let a user entered the physics marks incorrect 43, insted of 56
stu1.phy = 56 # changed the marks of physics
print(stu1.phy)
print(stu1.percentage)  # now problem is that when we calculate the percentage after re entering marks, percentage is calculated according t the previous marks, but we want to chnge percentage as will. 
# for this we use @property decorator on any method in the class to use the method as a property,
# means that when an attribute value depends on any function we can make this funtion to property like below

class stdnt:
    def __init__(self, Math, Phys, Bio):
        self.Math = Math
        self.Phys = Phys
        self.Bio = Bio

    @property
    def cal_percentage(self): # now this function is a property( attribute)
        return str((self.Math+self.Phys+self.Bio)/3) + "%"
stu2 = stdnt(67, 43, 32)  # object callingn
print(stu2.cal_percentage)   # this function became property   attribute

stu2.Phys= 56  # chnged the makrs from 43 to 56
print(stu2.cal_percentage)  # now percentage will also reset according to new entery



# There are two more decorator @getter and @setter we will discuss them
# What is Polymorphism?

# Polymorphism means “many forms”.
# In Object-Oriented Programming (OOP), polymorphism allows the same function, method, or operator to behave differently depending on the object or data type it is acting on.


# *********************Operator Overloading************************

# Operators like +, -, *, etc., are polymorphic —
# they behave differently for different data types.
# Python lets you overload operators in custom classes using special methods (also called magic methods or dunder methods like __add__, __sub__, etc.)


class Complex: # we wana create a class for complex numbers:
    def __init__(self, real, img):  # real and img is re parts of complex number as real part and imaginarry part
        self.real = real
        self.img = img
    def showNumber(self):
        print(self.real, "i +", self.img, "j")  # this function will show the syntex of complex nubmer

    def add(num1, num2):  #here num1 means self, In this funtion we are going to make logic to add two complex numbers
        newReal = num1.real+num2.real
        newImg = num1.img+num2.img
        return Complex(newReal, newImg)
    def __add__(num1, num2):  #here num1 means self, In this funtion we are going to make logic to add two complex numbers
        newReal = num1.real+num2.real
        newImg = num1.img+num2.img
        return Complex(newReal, newImg)
num1 = Complex(4,5)
num1.showNumber()

num2 = Complex(7,3)
num2.showNumber()
# above we take two real numbers in a class and now we wana add them, there is no builtin way to add them like for int, list, string, so for adding real numbers we have to overload an operator acccording to our need using dunder functions

num3 = num1.add(num2) # as we write a function to add complex numbers but the problem is that here we write "num1.add(num2)" for addition insted of num1+num2, for this we use dunder function as for add function dunder function is __add__,
num3.showNumber()

num4 = num1+num2  #since we mamde a dunder function in class so now we can perform addition like this
num4.showNumber()


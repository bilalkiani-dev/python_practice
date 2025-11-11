#***********************practice class & objects********************************


# classes objectsm], constructor, method


# Create student class that takes name and mrks of 3 subjecs as arguments in constructor. then create a method to print the average.

class Student:
    def __init__(self,name, pmarks, cmarks, umarks):
        self.stu_name = name
        self.physics_marks = pmarks
        self.chemistry_marks = cmarks
        self.urdu_marks = umarks

    def call_Avg(self):
        self.avg = (self.physics_marks+self.chemistry_marks+self.urdu_marks)/3
        print( "average marks are: ", self.avg)

s1 = Student("Bilal Kiani", 45, 32, 87)
print(s1.stu_name, s1.physics_marks, s1.chemistry_marks, s1.urdu_marks)
print(s1.call_Avg())

# same question by by passing mrks as an argument as list

class Studentt:
    def __init__(self, name, marks):
        self.student_name = name
        self.student_marks = marks

    def get_avg(self):
        sum = 0
        for value in self.student_marks:
            sum +=value
        print("Hy ", self.student_name, "your average score is: ", sum/3)
stu1 = Studentt("Bilal Kiani", [45, 89, 43])
stu1.get_avg()





#  ***************8 static method ***********************

class print_hello():

    @staticmethod
    def show():
        print("Hello Bilal !")
    show()    
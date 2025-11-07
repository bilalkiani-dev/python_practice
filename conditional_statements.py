# if    elif    else




#                      traffic light code
light = input("Enter light colorF: ")

if light == "green":
    print("go")
elif light == "red":
    print("Stop")
elif light == "yellow":
    print("Look")
else:
    print("Light is broken and not working")






#                                  write a code to grade students based on marks

marks = int(input("Enter marks of subject: "))


if marks>=90:
    print("You got 'A' grade")
elif marks>=80 and marks<90:
    print("you got 'B' grade")
elif marks>=70 and marks<80:
    print("you got 'C' grade")
elif marks>=60 and marks<70:
    print("you got 'D' grade")
elif marks>=50 and marks<60:
    print("you got 'E' grade")
else:
    print("Sorry you are fail")



#                                                 nesting

age = int(input("enter age: "))

if age >= 18:
    if age>=70:
        print("cannot drive")
    else:
        print("Allowed to drive")
else:
    print("under age, cannot drive")









 #                                     write a code to check if number is even or odd


number = int(input("Enter number: "))

if number%2==0:
    print("Given number", number, "is even")
else:
    print("Given number", number, "is odd")








#                                      write a program to check greatest of 3 numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1>num2 and num1>num3:
    print(num1, "is greater")
elif num2>num1 and num2>num3:
    print(num2, "is greater")
else:
    print(num3, "is greater")







 #                                 check number is multiple of 7 or not

numbr = int(input("Enter number: "))

if numbr%7==0:
    print("Given number", numbr, "is multiple of 7")
else:
    print("Givern number", numbr, "is not multiple of 7")
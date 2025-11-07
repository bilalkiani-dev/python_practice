# #*****************************FUNCTIONS****************************#
# #is the block of statements tht performs the specific task, can be useful to redduce redundent code

# #syntex:      def  func_name(parameter1, parameter2, ...):
# #                            some work to performs,  statements
# #                            return value

# #to perform task in function we call that function, syntex for function call is below
# #syntex:    func_name(arg1, arg2, ..)

# #Example: 

# x=20
# y=30
# def sum(a, b):
#     s = a+b
#     return s

# print(sum(x,y))


# #calculate average of 3 numbers using function
# x = int(input("Enter first number: "))
# y = int(input("Enter Second number: "))
# z = int(input("Enter third number: "))

# def calc_avg(a,b,c):
#     average = (a+b+c)/3
#     return average
# print("Average of Given three numbers is: ", calc_avg(x,y,z))

# #default parameters in functions
# # these are used when we wana perform function task without pasing arguments,   we assigns values to the parameters in function like
# def multi(a=2,b=2,c=2):#default parameters when we didnt passed any argument
#     m=a*b*c
#     print("Multiplication is: ",m)

# multi()#when no argument result will be according to default parameters as "8"
# multi(6,4,9)#when we pass arguments result will be according to the argument values not default values as "216"


#****************************practice Questions*******************************


# #write a function to print the length of a list,  list in parameters


# names = ["Bilal Kiani", "Saood Ahmed Sheikh", "Shabbar Alam", "Afan Hafiz"]
# def print_list(list):
#     print("length of given list is: ", len(list))

# print_list(names)



# #write a function to print the elements of list in a single line, list in parameters

# names = ["Bilal Kiani", "Saood Ahmed Sheikh", "Shabbar Alam", "Afan Hafiz"]

# def print_items(list):
#     for item in list:
#         print(item, end=" ")
# print_items(names)


# #write a function to print the factorial of n,  n in parameter
# n = int(input("Enter number to print factorial: "))

# def find_factorial(a):
#     factorial=1
#     for i in range(1, a+1):
#         factorial*=i
#     return factorial
# print("Factorial of Given number", n, "is: ", find_factorial(n))


# #write a function to conert the USD to PKR
# USD = float(input("Enter USD: "))

# def convert_usd(amount):
#     PKR = 281.2*USD
#     return PKR
# print(USD, "USD in PKR = ", convert_usd(USD))


# #write a function to return odd if given number is odd and return even if given number is even,    numbere in parameter
# number = int(input("Enter number: "))
# def even_odd(n):
#     if n%2==0:
#         return "even"
#     else:
#         return "odd"
# print("Given number is : ", even_odd(number))





##############********************RECURSION*******************########################

#recursion is when function calls it self repetidely, it works like a loop, Example below

#*******comparisen between loop and recursion**********

# #print numbers from n to 1 using for loop
# n = 10
# for i in range(n, 0, -1):
#     print(i, end=" ")

# # now same work using recursion
# m = 10
# def show(a):
#     if(a==0):
#         return
#     print(a)
#     show(a-1)
# show(m)

# in recursion we have to use base case ( if statement in previous program and then return)  to stop exiuting. otherwise this will infinitely exicute




# #calculate factorial using recursion
# n = 5
# def cal_fact(a):
#     if a==0 or a==1:
#         return 1
#     else:
#         return a*cal_fact(a-1)
# print(cal_fact(n))



# #write a recursive function to calculate the sum of first n netural numbers

# n = 10
# def cal_sum(a):
#     if a==0:
#         return 0
#     else:
#         return cal_sum(a-1) + a
# print("sum is: ", cal_sum(n))



# #print elements in list using recursive function

# names = ["bilal kiani", "Afan Hafiz", "Shabbar Alam", "moeen awan"]

# def print_items(list, idx):
#     if idx==len(list):
#         return
#     print(list[idx], end= " ")
#     print_items(list, idx+1)
# print_items(names, 0)
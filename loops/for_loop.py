# #for loops are used for sequential travel like traversing list, tuple, string etc
# #syntex:  for variable_name in list1.    this syntex is for any list named list1
# #eg:

# list1 = [1,2,3,4,5,6,7]
# for value in list1:
#     print(value)

# #same we can use for tuple like
# list1 = (1,2,3,4,5,6,7)
# for value in list1:
#     print(value)

# #same for string like
# name = "Bilal Kiani"
# for char in name:
#     print(char)

# # in for loop here is a concept for else part we use in for loop and it's completely optional
# for char in name:
#     print(char)
#     if char=="K":
#         print("K found in string")
#         break
# else:
#     print("END")



# # ****************practice questions***************

# #search for a number x in this tuple using for loop, (1,4,9,16,25,36,49,64,81,100)

# tuple1 = (1,4,9,16,25,36,49,64,81,100,16)
# x = 16
# idx = 0
# for i in tuple1:
#     if x==i:
#         print("Value found at index", idx)
#     idx+=1





# #     Important functions 

# #range()
# #range function returns a sequence of numbers, starting from 0 by default and increment by 1 by default and stops before specified number range.
# #Example: 

# #syntex:   for var_name in range(ending point)
# for el in range(5):  # this formate means we give range from 0 to 4,  this will print before 5,
#     print(el)

# #we also can specify starting point of range like,
# #syntex:   for var_name in range(starting point, ending point)
# for el in range(10,30):   #this function will print from 10 to 29,  before 30
#     print(el)

# #as in for loop increment is by default 1, we can also specify increment size like 2,  3  like
# #syntex:    for var_name in range(starting point, ending point, increment size)
# for el in range(50,100,3):# as this function will print from 50 to 99, before 100 and in each iteration it will increment by 3
#     print(el)


# #we can also access values in range by indexes like

# value = range(10)
# print(value[5])

# value1 = range(30,50,3)
# print(value1[5])
# print(value1[2])


# #         Solve using for and range()

# #print number from 1 to 100
# for i in range(1,101):
#     print(i)


# #print number from 100 to 1
# for i in range(100,0,-1):
#     print(i)


# #print multiplication table of number n

# n= int(input("Enter number to print table: "))

# for i in range(1,11,1):
#     table = n*i
#     print(n,"*",i,"=",table)

# #                                      pass statement in loop

# #pass statement in for loop is used to do nothing in loop, it is the null statement, 
# #pass sttement is used when sittuation arrives where we didn't want to do in loop, it can be used as placeholder for feature code.
# for val in range(1,21):
#     pass   #this loop will do nothing now we can write any code  after this loop
#            # but if we didn't use pass statement and not doing any work in loop then code after this loop will give error,
#            # we have to give some task in loop, so in this conditiion we use pass statement.




# #  print sum of first n numbers using for loop

# n=10
# sum= 0
# for i in range(n+1):
#     sum+=i
# print("total sum: ", sum)
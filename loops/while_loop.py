# #syhtex:     while condition:
#                  #some work, statements

# i = 1
# while i<=10:
#     print("Bilal Kiani", i)
#     i+=1

# # we can start our loop in reverse like
# i=10
# while i>=1:
#     print("Bilal Kiani", i)
#     i-=1


#************practice Questions***********


# #print multiplication table of nubmer n

# n = int(input("Enter number to print table: "))
# i = 1
# while i<=10:
#     table = n*i
#     print(n,"*",i,"=",table)
#     i+=1

# #print the element of following list using loop  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# list1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# count = 0
# while count<len(list1):
#     print(list1[count])
#     count +=1

# #search for a number x in this tuple using loop  (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# tuple1 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x=36
# i=0
# while i<len(tuple1):
#     if tuple1[i]==x:
#         print("Found at index ", i)
#         break
#     i+=1
# #"break" keyword in while loop is used to terminate the loop, like in previous example if we didn't use "break" 
# # statement then loop will search the whole tuple even after founding but if we use break statement then loop will
# #termintae after the first found. will not search the whole tuple


# # "continue" statement in while loop is used to only terminate exicution on current iteration and then continue with next iteration , example below

# i=1
# while i<=5:
#     print("Bilal Kiani",i)
#     i+=1
#     if i==3:
#         i+=1
#         continue #here we make a condition if i==3 don't exicute it continue to next iteration,  same this code skiped the iteration 3



# # print even number from 1 to 100
# i=1
# while i<=100:
#     if i%2!=0:
#         i+=1
#         continue
#     print(i)
#     i+=1




# #   write a program to find the sum of first n numbers using for loop

# n=10
# i=0
# sum=0
# while i<=n:
#     sum+=i
#     i+=1
# print("total sum: ", sum)

#find factorial of first n numbers usig for loop

n= int(input("Enter numberr to fing factorial: "))
factorial=1
for i in range(1,n+1):
    factorial*=i
print("Factorial of numer ",n,"= ", factorial)
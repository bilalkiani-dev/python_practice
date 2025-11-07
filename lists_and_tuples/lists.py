# #                                    lists   (Arrays in other languages like java   c++)

# marks = [45, 87, 64, 93, 73, 42, 98, 83, 73, 90]
# print(len(marks))
# print(marks)

# print(type(marks))

# print(marks[0])


# #we can store multiple types of data in list like   int,  float,   string.     in other languages like c++ we can only store same type of data in list or array

# #here a student with name as string type roll no as int  type degree program as string tye and CGPA as float type,   we cannot do this in other languages like c++

# student= ["bilal", 103, "BS&CS", 3.21]

# print(student)

# #relating to string( strings are immutible means cannot change string chractors  but lists are muteable means we can change elements in lists)
# student[0] = "saood"
# print(student)

# #slicing same like strings
# print(marks[2:6])
# print(marks[:4])
# print(marks[5:])

# #slicing as negative indexes same like strings

# print(marks[-9:-4])
# print(marks[-10:])


# #some functions can be performed on lists

# #our list of marks is
# print("list of marks:\n", marks)

# marks.append(92)  #it adds element at the end of list
# print(marks)
# marks.sort()    #it sorts the list in assinding order
# print(marks)
# marks.sort(reverse=True)   #it sorts list in decending order
# print(marks)
# marks.reverse()   #it reverse the whole string
# print(marks)

# #         syntex: (list.insert(index, element)     )
# marks.insert(4, 45)   # it inserts element in lis at specific index
# print(marks)

# marks.remove(73) # it removes first occurance of specific element
# print(marks)

# #     syntex:   list.pop(index)
# marks.pop(5)   #it removes element at specific index




#                         ***************practice Questions***************


# #           write a program to ask the user to enter names of three movies and store them in a list


# movie1 = input("Enter firts movie name: ")
# movie2 = input("Enter second movie name: ")
# movie3 = input("Enter third movie name: ")

# movies = []

# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)
# print(movies)


#                      write a program to check the list is palandrom or not

list1 = [1, 2, 3, 2, 1]
copy_list = list1.copy()
copy_list.reverse()

if list1 == copy_list:
    print("list is palandrom")
else:
    print("list is  not palandrom")
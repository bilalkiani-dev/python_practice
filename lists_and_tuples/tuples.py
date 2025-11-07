# # tuples works same like lists with some differences
# #difference is that  list are mutable that can be changed but tuples are immutable that cannot be changed
# # syntex: tuple_name = (elements like list)

# marks = (45, 24, 23, 92, 82, 23, 42, 73, 63)
# print(marks)

# #marks[5] = 74       not allowed

# print(len(marks))
# print(type(marks))

# #we can access elements by index same like string and list
# print(marks[5])

# #slicing same like strings and lists
# print(marks[0:5])
# print(marks[5:])

# #some function can be performed on tuples

# #                   tuple.index()
# #syntex:   tuple.index(element)
# print(marks.index(42))    #it returns the index of first occurance of searched element
# #                 tuple.count()
# #syntex:    tuple.count(element)
# print(marks.count(23))     #it counts the occurance of searched element






#                         ***************practice Questions***************


# average_result = sum(marks)/len(marks)

# print("average result is: ", average_result)

# total_marks = sum(marks)

# print(total_marks)


# new_marks = marks+(67, 67)
# print(new_marks)






#            write a program to count the number of students with grade A in the following tupple
grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))
#store the above values in a list and sort tehm as "A" to "D"

grade_list = []
grade_list.append(grade[0])
grade_list.append(grade[1])
grade_list.append(grade[2])
grade_list.append(grade[3])
grade_list.append(grade[4])
grade_list.append(grade[5])
grade_list.append(grade[6])

grade_list.sort()
print(grade_list)
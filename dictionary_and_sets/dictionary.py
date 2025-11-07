student = {
    "name" : "Bilal Kiani",
    "Roll NO" : 103,
    "Class" : "BS&CS",
    "CGPA" : 3.21,
    "promoted" : True,
    "skills": ["python", "C++", "java"],
    "topics": ("dictionary", "sets")
}

print(student)
print(type(student))

#access dictionary elements
print(student["name"])

# #           if we try to access any key that is not vilabel in dictionary it will give error like
# print(student[father_name])    #will give error

# dictionary is mutiable so we can change values in dictionary like

student["name"] = "saood Ahmed"
print(student["name"])
print(student)


#        we can also add new key with value in dictionary like
student["subjects"] = ["DLD", "OOPS", "DSA"]
print(student)    # syntex of Assigning new value and creating new key with value is same

#    we can create null dictionary like
student2 = {}
#    we can add keys with values in dictionary when required
student2["name"]= "shabbar Alam"
student2["CGPA"]= 3.00
print(student2)


#   we can do nesting in dictionary like
student3 = {
    "name": "Afan",
    "roll no": 68,
    "subjects_marks":{
        "OOPS": 76,
        "DSA":  86,
        "programming_fundamentals": 73
    }
}
print(student3)
#    we can access nesting key values in that way like

print(student3["subjects_marks"]["DSA"])  # it prints marks of subject "DSA"

#   we can also print just student_marks
print(student3["subjects_marks"])


#     ********* some functions we can use for dictionary

print(student.keys())         #this function returns all keys in dictionary

print(student3.values())      #this function returns all values in dictionary

print(student2.items())       #this function returns pairs fo key and value as tuples
# we can type cast these tuples of dictionary values like
print(list(student2.items()))   #it will return pairs of key and values tuples in a list
# and we can access any key value pair in a list using index like
pairs = list(student2.items())  #we stored list of dictionary tuples in variable   Pairs
print(pairs[1])  # it will print the key value pair as tuple at index 1   means second tuple pair


print(student3.get("name"))  #this function return the value of searched key.   nwo here is one more way to access value using key that we already discussed above like
print(student3["name"])    #this will also print the same valuse as above.
#            but the difference is if we search key that is not available in dictionary then first method will return "none" and second method will give error like
# print(student3.get("CGPA"))   # will return none value
# print(student3["CGPA"])   # will give error


student3.update({"CGPA": 3.00})   #this function will add new dictionary key value in dictionary
print(student3)
#  also we can do this like

new_student = {"CGPA": 3.00}    #storing cgpa in new dictionary
student3.update(new_student)   # adding new_student dictionary values in previous student3 dictionary
print(student3)


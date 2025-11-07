#sets is the colection of unordered items, elements means they don't have indexes,
#each element in set must be unique and immutable
#sets are mutable but elements of set are immutable means we can add or remove element in set but cannot change element in set
#syntex:   set_name = {element1, element2, ...}
#we can store any type of data elements in set except list and dictionary because list and dictionary are mutable but the set is immutable
#sets contains unique values, if we write duplicate values it will stores only once and counts only one value for duplicate value


student = {"Bilal kiani", 103, 3.21, "BS&CS"}
print(student)
print(type(student))
print(len(student))

#if we try to create empity set like     set_name = {}     thsi is the syntex of dictionary for empity dictionary. and this willl be considered as dictionary type not set.
student1 = {}
print(type(student1))    #considered as dictionary not set
 
#so to create empity set the syntex is:     set_name = set()
student2 = set()
print(type(student2))   # correct syntex of empity set



#   **************some functions or methods can be used for sets like

#since set is mutable so we can add or remove elements in it like
student2.add("afan")   # this .add functions is used to add new element in set
student2.add(68)
student2.add(3.00)
student2.add("BS&CS")
student2.add(("OOPS", "DSA", "programming fundamentals"))   # tuple type element in set

print(student2)


#removing element

student2.remove("afan")   #this function will remove the specific element
# if we tryp to remove element that is not in set it will give error


student2.pop()   #this function will remove random element in set
print(student2)
print(student2.pop())   #prints the random removed value

student2.clear()  # this function will empity the whole set
print(student2)


# now two more important methods in set are union and intersection

#union method will combine two set values and give us unique values in two sets if both have common values like
set1 = {1,2,3,4}
set2 = {3,1,5,6}
print(set1.union(set2))   #will returns new set didn't make changes in old sets

#intersection method will combine both sets and returns only common values in both sets lke
print(set1.intersection(set2))  #will returns new set and not changes the old sets same like union
#*********************practice file i/O**********************


#create a new file "practice.txt" using python. Add the following data in it:
# Hi everyone
# we are learning file I/O
# using java.
# i like programming in java.

with open("practice.txt", "a") as file:  #this will create nd open file in append mode
    file.write("hi every one")
    file.write("\n we are learning file I/O")
    file.write("\n usng java")
    file.write("\n i like programming in java.")


#write a function that relace all occurance of "java" with "python" in above file.
with open("practice.txt", "r") as file:
    data = file.read()    #data is stored in variable "data" in form of string
new_data = data.replace("java", "python")  #this will replace java to python as in 
print(new_data)
#now we also have to over write in file "practice.txt"
with open("practice.txt", "w") as file:
    file.write(new_data)   #data over writed



# write function to search the word "learning" exist or not in file
word = "learning"
def search_for_word():
    with open("practice.txt", 'r') as file:
        data = file.read()
        if(data.find(word)!= -1):
            print("found")
        else:
            print("not found")
search_for_word()



# write a function to find in which line of the file doees the word "learning" occur first.  print -1 if word not found
def find_line():
    data = True
    line_no = 1
    with open("practice.txt", 'r') as file:
        while data:
            data = file.readline()
            if(word in data):
                return line_no
            line_no+=1
    return -1
print(find_line())



#from a file containingn numbers separated by comma, print the count of even numbers.
# we have data in file "numbers.txt"
#methond 1:

with open("numbers.txt", 'r') as file:
    data = file.read()
    print(data)
    num= ""
    for value in range(len(data)):
        if(data[value]==","):
            print(int(num))
            num = ""
        else:
            num+=data[value]
            #this progrma only printed numbers as integer individually


#method 2;
with open("numbers.txt", 'r') as file: 
    data = file.read()
    print(data)
    list1 = data.split(",")    #split is builtin function that will return value befor , individually
    print(list1)
    count = 0
    for value in list1:
        if int(value)%2==0:
            count +=1
print(count)
import os
#python can be used to perform operation on file in computer (read and write)
#files can be of different formate:
#Text files: .txt   .docx    .log etc
#Binary files: .mp4    .mov     .png    .jpeg   etc

#we have to open file before read and write operation, for this we have builtin functions in pythhon,



#syntex of opening:  open("file name", "mode")
#in python for fileI/O ther are many modes for the operation like
#"r" :   open for reading  (default)
#"w" :   open for writing, truncating the file first (means when wirting data in file the whole data file will be delated and the new data will be added called over writing)
#"x" :   create a new fiel and open it for reading
#"a" :   open for writing, appending to the end of data file if it exist
#"b" :   binary mode
#"t" :   text mode (bydefault), means when we opening any file by "r" this will by default opens files as text,  we have to sepcify to open other formate
#"+"  :   open a disk file for updating (read and write): means:   r, means opening for reading but r+ means opening for  read and write,   a for append  and a+  for append and read   etc


# #*****************Read operation*****************************
# f = open("python.txt", "r")   #here we opened the file for read operation,   if we didn't give mode    by default it will be opend for read, now we can make read operation on that file
# data = f.read()   #this read function will return our file text data as whole, in stored in data named variable.
# print(data)
# print(type(data))
# f.close()   #when opened the file and after performing operation we should close the file to avoid resourse issue
# #or better practice is to write like,
# with open("python.txt", "r") as f:   # using This way, Python automatically closes the file after reading.
#     data=f.read()
#     print(data)

# #more operation on read file:
# data2= f.read(23)   #used to read only first 23 letters in data,  23 is number of letters we can write number to which we wana print
# data3= f.readline()  #used to read line by line
# #important thing,  when we already read the text from file then next time printing we will see only emipty data  because when once data readed next time this wil not print,  we have to close the file and then next time will start from start


# #*******************writing to a file********************
# # two methods:  "w" for over write   and   "a"   for append to next
# file = open("python.txt", "w")
# newdata = file.write("this is a new file")
# print(newdata)   #this will not run because we opened this file only wor write, but new data in file has been updated
# file.close()    #close the file

# #for append
# file2 = open("python.txt", "a")
# newdata1 = file2.write(". this is the appended data to next")
# newdata2 = file2.write("\n data in next line")
# file2.close()

# #and if we wana open a file that doesnot exist then python will outomatically create that file for us like
# file3 = open("sample.txt", "w")  #by this new file "sample.txt"  will be be created automatically in our project folder
# file3.write("new file created")  #data added in new file


#one important thing:  as we see that the file opening for the operation within the same project folder
#but if we opens a file that is out of same folder then we nedd to give the whole path of that file like
#i have a file named "demo.txt" in that path in pc "E:\universty documents\Machine learning\demo",  we have to specify whole name,

demofile = open(r"E:\universty documents\Machine learning\demo\demo.txt", "r")
demodata = demofile.read()   #will return whole data from that file
print(demodata)
demofile.close()


#********combined modes **************
# we know thaat "r"  for read mode  and we can use "r+"  for both read nd write mode like

file4 = open("sample.txt", "r+") #for read and write mode
file4.write("new sammple data added")
print(file4.read())
file4.close()

file4 = open("sample.txt", "w+")   #write plus read
print(file4.read())
file4.write("new data added")
file4.close()   
#etc


#*****************Deleting a file*******************
#we dont have any as such operation to delete file , we use and os module to delete file as:
#we have to import os module as i imported at the top  "import os", now we can delete file
#as i have a file "delete.txt" in same folder and i wana  delete it
os.remove("delete.txt")   #file has been deleted

#we will do practice in new file named "file_io_practice.py"
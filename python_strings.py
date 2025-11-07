str1 = 'bilal'
str2 = "kiani"
str3 = """bilal kiani"""

final_str = str1+" "+str2
print(final_str)
print(len(final_str))



#fitching indexes of string
print(final_str[3])


#slicing in strings
print(final_str[0:5])
print(final_str[6:11])

print(final_str[ :5])
print(final_str[6: ])


#reverse accessing strings

print(final_str[-11:-6])
print(final_str[-5:-0], "\n")

print(final_str[:-6])
print(final_str[-5:])






#                                               string functions


#checks string ending with specific substring
print(final_str.endswith("ni"))


#captilize first charactor
print(final_str.capitalize())


#replace all string charactors with new
print(final_str.replace("bilal kiani", "junaid khan"))


#finds specific word, if found it returns first indes of that word
str = "hy my name is bilal kiani, my little brother name is waseem kiani and my father name is rakhamtullah kiani"
print(str.find("kiani"))


#counts occurance of substring in a string
print(str.count("kiani"))



#print length of string
print(len(str))
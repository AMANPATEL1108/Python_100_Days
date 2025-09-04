str="amanpatel  !!!"
print(len(str))
print(str.upper())
print(str.lower())
print(str.rstrip("!"))
print(str.replace("amanpatel!","Ap"))
print(str.split(" "))

name="my name is aman patel"

print(name.capitalize())

print(str.center(50))

print(name.count("a"))
print(str.endswith("!"))
print(str.find("ama")) #not found -1

# print(str.index("asdacs")) #not found Exception
name1="asdsd"
print(name1.isalnum())

a="sdfsdfc\n"
print(a.isprintable()) #check not is a \n like this in  a string

#is title for word first letter  capital checking
#swapecase lowet to upper upper to lower case 
#title check do a first letter of check a Capital
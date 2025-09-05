# a=int(input("Enter your age:"))
# print("your age is :",a)


# print(a>18)
# print(a<18)
# print(a==18)
# print(a!=18)

# if(a>18):
#     print("You can Drive")
# else:
#     print("You Can Not Drive")


# applePrice=200
# budget=200

num=int(input("ENter a Num Value"))

# if(num<0):
#         print("Add 1 Kg Apple")
# elif (num==0):
#     print("Number is Zero") 
# else:
#      print("Number is Positive")    




#nested If Else
if(num<0):
    print("number is Negative")
elif(num>0):
    if(num<=10):
        print("Number is Between 1-10")
    elif(num>10 and num<=20):
        print("Number Between 11-20")
    else:
        print("Number is Greter then 20")
else:
    print("Number is Zero")
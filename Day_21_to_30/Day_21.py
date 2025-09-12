def average(a=9,b=3):   #default arg
    print("The average is",(a+b)/2)

average(5,6)


def nameis(*name):
    for nam in name:
        print("name is ",nam) 
name=["aman","dev","patil"]
nameis(*name)
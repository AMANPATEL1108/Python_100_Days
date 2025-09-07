
x=int(input("Enter a Value of X:"))

match x:
    case 0:
        print("Zero")
    case 4:
        print("Four")   
    case _ if x!=90:
        print("!90:",x)
    case _ if x!=80:
        print("!70",x)
    case _ if x!=70:
        print("!=70",x)
    case _:
        print(x)
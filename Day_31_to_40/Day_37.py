def func1():
    try:
        l=[1,2,3,5,7,8]
        i=int(input("Enter a Index:"))
        print(l[i])
        return 1
    except:
        print("Some error Occure")
        return 0        #here not return then then executre without finally here after apply finally here after return a called a finally also 
    finally:
        print("I am Always Executed")

x=func1()
print(x)
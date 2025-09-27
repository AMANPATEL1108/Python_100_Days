a=input("Enter a Number:")
print(f"Miltiplicatin table of {a} is :")


try:        
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a) * i}" )
except Exception as e:
    print(e)


print("Some lines of code ")
print("End Program") 
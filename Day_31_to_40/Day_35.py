print("-----------------For Loops----------------")
for i in range(5):
    print(i)
    if i==4:
        break
else:
    print("Sorry no i",i) #use a loop for end not a break


print("---------------While Loop-------------------")

i=0
while i<7:
    print(i)
    i=i+1
    if i==4:
        break
else:
    print("Sorry fro while",i)
import random
'''
1 frforo snack 
-1 for water
0 for gun
'''
computer = random.choice([-1,0,1])
youstr=input("Enter your code")
youDict = {"s":1,"w":-1,"g":0}
reverseDict={1:"snack",-1:"water",0:"gun"}
you=youDict[youstr]
print(f"You Choose{reverseDict[you]} \n Computer choose {reverseDict[computer]}")

if(computer== you):
    print("Draw")
else:
    if(computer == -1 and you == 1):
        print("You Won")
    elif(computer ==-1 and you ==0):
        print("You Lose")
    elif(computer == 1 and you == -1):
        print("You Lose")
    elif(computer ==-1 and you ==0):
        print("You Won")
    elif(computer == 0 and you == -1):
        print("You Won")
    elif(computer ==0 and you ==1):
        print("You Lose")
    else:
        print("some thing wrong")
    
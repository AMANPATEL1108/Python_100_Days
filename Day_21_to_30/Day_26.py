import time

timestamp=time.strftime('%H:%M:%S')
print(timestamp)

hour=int(time.strftime('%H'))
minitue=int(time.strftime('%M'))
second=int(time.strftime('%S'))


# print(hour)
# print(minitue)
# print(second)

if(hour >= 6 & 12 < hour):
    print("Good Morning Aman")
elif(hour >= 12 & 17<hour):
    print("Good Afternoon Aman")
elif(hour >= 17 & 12<hour):
    print("Good Evening Aman")
elif(hour > 21 ):
    print("Good Night Aman")

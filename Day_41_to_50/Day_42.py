marks=[12,54,34,76,32,54,32,76,89,21]

# index=0
# for mark in marks:
#     print(mark)
#     if(index==3):
#          print("Ohh ,awesome !")
#     index+=1

for index,mark in enumerate(marks,start=1):
    print(index,mark)
    if(index==3):
         print("Ohh,awesome !")
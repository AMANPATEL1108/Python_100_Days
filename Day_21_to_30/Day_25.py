tuplel=("Spain","India","England","UK")

temp=list(tuplel)
temp.append("Russia")
temp.pop(3)
temp[2]="Finland"
tuplel=tuple(temp)
print(tuplel)
print(tuplel.count("India"))

# res=tuplel.index(3,4,8) #3 is 4 to 8 index range find 
# print(res)

print(len(tuplel))
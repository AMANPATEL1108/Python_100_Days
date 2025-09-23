s1={1,2,5,6}
s2={3,6,7}

print(s1.union(s2))
s1.update(s2)
print(s1)


c1={1,2,3,4,5}
c2={3,4,5,6}
print(c1.intersection_update(c2))
print(c1.symmetric_difference(c2))

#Disjpint -not same then return true-false
#super set-all element in 2nd that all return true-false
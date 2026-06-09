# union ,intersection ,diff
set1 = {1,2,3,4,5}
set2 = {3,4,5,6}
print(set1. union(set2))
print(set1. intersection(set2))
print(set1. symmetric_difference(set2))
print(set1. difference(set2))

setA = {1,2}
setB = {1,2,3,4}
setC = {5,6}

print(setA.issubset(setB))
print(setB.issuperset(setA))
print(setA.isdisjoint(setC))

 # set unpacking
a,*b = set1
print(a)
print(b)
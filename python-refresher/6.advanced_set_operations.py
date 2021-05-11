friends = {"ram", "sujani", "suresh", "chalam"}

abroad = {"ram", 'sujani'}

local_friends = friends.difference(abroad)
print(local_friends)

a = {1,2,3}
b = {2,3,5,7}
c = {}

aandb  = a.intersection(b)
aandc = a.intersection(c)
aorb = a.union(b)

print(aandb)
print(aandc)
print(aorb)

set1 = {5, 14, 9, 31, 12, 77, 67, 8}
set2 = {9, 5, 12, 77}
print(set1.intersection(set2))

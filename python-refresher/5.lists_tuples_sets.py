list = ["ram", 'sujani', 'suresh']

tuple = ('ram', 'sujani', 'suresh')  # constant.  not able to change in future

set = { "ram", 'sujani', 'suresh' }   # no duplicate elements

print(list[0])

print(list)
list[0] = "smith"
print(list)

# print(tuple)
# tuple[0] = "Rambabu"  # gives error.
# print(tuple)

list.append('Chalam') # adds element at the last index
print(list)

list.remove('suresh')
print(list)


print(set)
set.add('amith')
print(set)
set.add('amith') # duplicates will not be added. therefore set will not be altered.
print(set)
set.remove('suresh')
print(set)

print(tuple)



# initialising single valued tuple 
tuple1 = (123,)   # need to append , at last position in order to differentiate between a maths equation. which means a tuple.
tuple1   = 123,   # which is also represents a single valued tuple.
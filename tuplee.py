# tuple ---> A built in data type that lets us create immutable sequences of values

tup =(1, 2435, 342, 35, 1, 1, 1)
print(type(tup))
print(tup)
print(tup[0])

#slicing in tuple same as list
print(tup[0:4])


#tup.index(element) ---> return index of first occurrence

print(tup.index(35))

#tup.count(element) ---> counts total occurrences
print(tup.count(1))


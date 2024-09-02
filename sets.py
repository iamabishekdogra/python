
# set is a collection of unordered items. sets are mutable
# Each element in the sets must be immutable and unique.
# we can not storer list or dict in sets becoz they are mutable.
# duplicate values are ignored

#collection = {1, 2, 3, 3, "Abi"}

#collection.add(1)
#collection.add((1, 2))
#collection.add("python")
collection1 = {2, 3, 4, 5}
collection2 = {1, 3, 4, 5, 6, 7}
print(collection1.union(collection2)) # combine both set value and return new
print(collection1.intersection(collection2)) #combine common values and return new

#collection.pop() #remove random value

print(collection1)

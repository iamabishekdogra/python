# lists and tuple
studentdata = [ 23, 45, 64, 45, 54]
print(studentdata)

# slicing of list
print(studentdata[0:4])
print(type(studentdata))

# list methode
#list.append ---> add one element at the end
studentdata.append(5)
print(studentdata)

#list.sort ----> sort in ascending order
studentdata.sort(reverse=True) #sort in descending order
print(studentdata)

fruit = ["banana", "apple", "lithi"]
print(fruit)

fruit.sort(reverse=True)
print(fruit)

#list.reverse ----> reverse list
studentdata.reverse()
print(studentdata)

#list.insert(index, value)  ----> insert element at index

studentdata.insert(1, 5654)
print(studentdata)

#list.remove(1) ---> remove first occurrence of element
studentdata.remove(45)
print(studentdata)

#list.pop(index) ---> remove element at index
studentdata.pop(1)
print(studentdata)

#E.g
movies =[]
movies.append(input("enter your first movie : "))
movies.append(input("enter your 2nd movie : "))
movies.append(input("enter your 3rd movie : "))

print(movies)


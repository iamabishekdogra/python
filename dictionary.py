# dictinary are used to store data values in {key:value} pairs,
# they are unordered, mutable(changeable) & don"t allow duplicate keys
# key can be float, tuple, or integer
"""
info = {
    "name" : "Abhishek",
    "subjects" : ["python", "java", "C++"],
    "topics" : ("dict", "sets"),
    "age" : 35,
    "is_adult" : True,
    "marks" : 94.4
}

null_dict = {}
print(null_dict)
null_dict["Name"] = "Abhishek"
null_dict["surname"] = "Dogra"
print(null_dict)

"""
#nested Ditionary

students = {
    #Keys:value
    "name" : "Abhishek",
    "Surname" : "Dogra",
    "subjects" : {
        "phy" : 67,
        "chem" : 34,
        "Math": 99

    }
}
new_Dict = {"City" : "Hamirpur"}
students["name"] = "Abhisek"  #overwrite
students.update(new_Dict)
print(students.keys()) #return all keys of dictionary , it not return nested keys only outer keys
print(students.values()) #return all the values
print(students.items()) #return all key and values in tuple
print(students.get("name")) #return the value of the key, we can add multiple values init


#conditional Statements (if-elif-else)
"""
light = input("light is : ")

if(light == "red"):
    print("Stop")
elif(light == "Yellow"):
    print("Look")
elif(light == "Green"):
    print("Go")
else:
    print("Light is broken")
"""
# question is [A=5 & G=M]   [A=2 & G=F]
A = int(input("A : "))
G = input("M/F : ")
if(A == 1 or A == 2 or G == "M"):
    print("fee is 100")
elif((A == 3 or A == 4) and G == "F"):
    print("fee is 200")
elif(A == 5 and G == "M"):
    print("fee is 300")

else:
    print("no fee")
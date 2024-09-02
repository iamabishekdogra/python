# function ---->  Block of statements that perform a specfic task

"""
syntax: 

 def func_name(para1, para2):  here def is use to define the function
     some work
   return value

func_name(arg1, arg2) ----> Function call



def  cal_sum(a, b):
    
     return a + b

sum = cal_sum(6, 4)
print(sum)


def print_hello():
     print("hello")

print_hello()



def cal_avg(a, b, c):
     sum = a + b+ c
     avg = sum/3

     print(avg)
     return avg
cal_avg(3, 5, 7)

"""

cities = ["delhi", "pune", "mumbai"]
heros = ["thor", "iron man", "captainA"]


def print_len(list):
     print(len(list))
     

def print_list(list):
     for item in list:
          print(item, end = " ")

print_list(heros)
print_list(cities)
print_len(heros)

def fact(n):
     fact = 1
     for i in range(1, n+1):
          fact *= i
     print("fact of", n, "number is", fact)

fact(6)

def dollar_conv(dollar):
     inr = dollar * 83
     print("The value of", dollar, "US dollar in Indian rupee is :", inr)

dollar_conv(5)
# write a function to calculate the factorial of n number

"""

def cal_fact(n):
   fact = 1
   for i in range(1, n+1):
      fact *= i
   print(fact)

cal_fact(5)


# WAF to find the factorial of n.

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")
    
converter(100)



# WAF to print the length of a list

cities = ["Delhi", "Mumbai", "Kolkata", "pune"]


def print_len(list):
    print(list)
    print(len(list))

print_len(cities)

"""

# write a funtion to check a no is odd or even

def check_no(n):
    n = int(input("Entre any no: "))
    if n%2 == 0:
        return "even no"
    else:
        return "odd no"
       
        
print(check_no(4))
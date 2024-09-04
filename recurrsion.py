# write a recursive function to add first n natural number
"""
def calc_sum(n):
    if n == 0:
        return 0
    else:
        return n + calc_sum(n-1)

print(calc_sum(5))

"""
# write a recursive function to print all the element in list


def print_list(list, idx=0):
    if(idx == len(list)):
        return 
    print(list[idx])
    print_list(list, idx+1)

fruits = ["orange", "banana", "guava", "lichi"]

print_list(fruits)
# loops are used to repeat  
# while loop



nums = [1, 3, 4, 6, 7, 21, 13, 6]
x = int(input("entre the no : "))
i = 0

while i < len(nums):
    #print(i)
    if (nums[i] == x ):
        print("found on index no", i)
        break
    else :
        print("finding....")
    i += 1
 
print("End of loop")

#print("end of loop")

# Break : used to terminate the loop when encountered
# continue : terminate executin in the current iteration And continues execution of the loop with the next iteration

#Break
i = 0
while i <= 5:
    if(i == 3):
        i += 1
        break

    print(i)
    i += 1

#continue
i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue

    print(i)
    i += 1


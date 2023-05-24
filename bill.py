 # def cube(num):
 #    return pow(num, 3)


#----------Take input from user for an array -----------#

from array import *

arr = array("i",[])
n = int(input("Enter the length of array: "))

for i in range(n):   #(01234.....)
    x = int(input("Enter array element: "))
    arr.append(x)

print(arr)

# val = int(input("Enter the value to search: "))
#
# k = 0
# for e in arr: #(9,0,8,7....)
#     if e == val:
#
#        print(k)
#        break
#
#     k = k+1
# # print(arr.index(val)) #using direct function
#
#  k = 0
#  for e in arr:
#      if e == val:
#          print("Value present in array")
#     else:
#         print("Value not in array")
#
#     k = k+1
# adding test line. Please delete it after

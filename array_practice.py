# #Takes input for an array and prints them . Then gives any input values index in the array#
#
#
# from array import *
#
# arr = array('i',[])
#
# n = int(input("Enter length of array: "))
#
# for i in range(n):
#     x= int(input("Enter array element: "))
#     arr.append(x)
#
# print(arr)
#
# val= int(input("Enter element to be searched: "))
#
# # k = 0            #Search the index for val in arr #
# #
# # for e in arr:
# #     if e == val:
# #         print(k)
# #         break
# #
# #     k+=1
#
# print(arr.index(val))   # Search the index for val in arr by direct fn#
#


#Given an array of n distinct integers and an element x , search the x element in array using minimum number of comparison#
#
# def search(arr , n, x ):
#     # 1st comparison
#
#  if arr[n-1] == x:
#     return "found"
#
#  backup = arr[n-1]
#  arr[n-1] = x
#
#  i=0
#
#  while (i<n):
#     if (arr[i] == x):
#
#         arr[n-1] = backup
#
#         if (i<n-1):
#             return"found"
#
#         return "not found"
#     i = i+1
#
#
#
# arr = [4,2,54,12]
# n = len(arr)
# x = 90
# print(search(arr, n, x))
# #

# arr = [4,2,54,12]
# x = 90
#
# if x in arr:
#     print("found")
# else:
#     print("Not found")
#
#


# print(2**3)
# print(2//4)
#
#
#
# print(2 is 4)
#
# import random
# print(random.randint(25,50))
#
# a = (1,11,2)
# x = sorted(a)
# print(x)
#
# a = ("h","b","a","c","f","d","e","g")
# x = sorted(a)
# print(a)



# print(sorted(list(a)))
# print(sorted(list(b)))

#anagram checker

# def check(a,b):
#     if len(a) != len(b):
#         return False
#     elif sorted(list(a)) == sorted(list(b)):
#          return True
#     else:
#         return False
#
# a = "iceman"
# b = "cinema"
#
# print(check(a,b))
#
#

# function for SUM:
#
# def sum(numbers):
#     total = 0
#     for num in numbers:
#         total += num
#         print("total sum is{}".format(total))
#
# print(sum(200))
# import time
# currenttime = time.localtime(time.time())
#
# print(currenttime)
#
# x="10"
# print(int(x))

# print(list(range(6)))
#
# for var in list(range(6)):
#     print(var)
# function to search an element in minimum number comparison


def search (arr, n, x):

# 1st comparison
  if arr[n-1] == x:
      return "found"

  backup = arr [n-1]
  arr[n-1] = x

  i = 0
  while(i < n) :

      if (arr[i] == x) :

           arr[n-1] = backup

           if (i < n-1):
               return "Found"

           return "Not Found"
      i = i + 1


arr = [4,6,1,5,8]
n = len(arr)
x = 6
print (search(arr, n, x))

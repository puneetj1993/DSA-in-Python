#-------Binary search----------------------------

#Binary Search can be used only for sorted lists
#We will find the mid point of the list
#If midpoint is the number then return it
#If no is smaller then midpoint then it means it is somewhere between 0th and mid-1 element
#If no is greater then midpoint then it means it is somewhere between mid+1 and last element
#Complexity O(logN) while for sequential/linear search it it O(n) hence Binary is more efficient then linear

#--------------Recursion Code-----------

def binary_search(l,item,start,end):
    if start>end:
        return False
    else:
        mid=(start+end)//2
        if item == l[mid]:
            return True
        elif item<l[mid]:
            return binary_search(l,item,start,mid-1)
        else:
            return binary_search(l,item,mid+1,end)

l=[3,12,13,14,15,16]
item=31
print(binary_search(l,item,0,len(l)-1))
-------------------using loop-------------
arr = [11, 12, 15, 18, 21]
num = 18
n = len(arr)-1
i = 0
while i <= n:
    mid = (i+n)//2
    print(mid, arr[mid])
    if arr[mid] == num:
        print("foound")
        break
    if num < arr[mid]:
        n = mid-1
    if num > arr[mid]:
        i = mid+1



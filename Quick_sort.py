#--------------Quick Sort-----------
# Just like merge sort or shell sort, this is a divide and conquer approach towards solving the sorting problem.
# In this case, the list which needs to be sorted is partitioned into smaller units.
# However, unlike the merge sort algorithm, this partitioning is not really based on the length of the original array or some artificial index value.
# But it is based on something which is called a pivot. A pivot is one of the elements which is picked from a list.
# The list is partitioned in such a manner that all the elements smaller than this pivot element goes to left side and bigger one on the right side of the list.
# Common practice is to take either the leftmost element in the list, the rightmost element, or the one in the middle of the list



# Complexity = nlog(n)(average Case) and logarithm over here has a base of 2, because we are subdividing our list into two equal parts at each iteration
# Space Complexity = O(log(n)), at least in the average case. The worst case space complexity for quick sort is O(n).
# This sorting is not stable as entities which are equal in value in the input array may be rearranged in the sorted array.
# Stable elements which are equal in value in the input array retain their order after the sorting has been performed.
# This sort is not adaptive. Adaptive means that algo can judge itself whether the list is already sorted and then break the loop or perform less operations if it is already sorted.
# So it doesn't matter what the original ordering of the elements is, the number of operations which quick sort performs will be the same


#-------------------CODE-----------------------------

def partition(l, start, end):
    
    
    pivot = l[start]
    leftmark = start+1
    rightmark= end

    while True:

        while leftmark<=rightmark and l[leftmark] <= pivot:     #Increment left mark till if find l[leftmark]> pivot
            leftmark+=1
        while leftmark<=rightmark and l[rightmark]>= pivot:     #Decrement right mark till if find l[rightmark]< pivot
            rightmark-=1
        if leftmark<=rightmark:                                 #If l[leftmark]>pivot and l[rightmark]<pivot then swap l[leftmark] and l[rightmark]
            l[leftmark],l[rightmark]=l[rightmark],l[leftmark]
            leftmark,rightmark = leftmark+1, rightmark-1
        else:                                                   #If leftmark>rightmark then break the loop
            break
            
            
    l[start],l[rightmark]= l[rightmark],l[start]                #After breaking the loop, swap pivot and rightmark element and now we can sat that pivot is sorted
    return rightmark                                            #Return rightmark position which will act as new pivot and list will be divided at this point

def quick_sort(l, start, end): 
    if start < end:

        pi = partition(l, start, end)

        quick_sort(l, start, pi - 1)                            #Sending left half of list
    
        quick_sort(l, pi + 1, end)                              #Sending right half of list

l=[11,23,45,67,54,3,6,2,1,8,0]
quick_sort(l,0,len(l)-1)
print(l)

#--------------Merge Sort-----------
# Merge sort adopts the process of divide and conquer, in order to create smaller and smaller problems until it gets to the point where we end up with single element sublists.
# Then we follow the conquer part to combine 2 single element sublists with each other and simultaneously sorting them
# Again, we compare 2 2 element sublists and sort and join them and so on.
# In this way we are getting sorted sublists at each iteration and then we are merging them together to get a complete sorted list.



# Complexity = O(nlogn) and logarithm over here has a base of 2, because we are subdividing our list into two equal parts at each iteration
# Space Complexity = O(n) as we create all of the sublists which we require for this
# This sorting is stable as entities which are equal in value in the input array are not rearranged in the sorted array.
# Stable elements which are equal in value in the input array retain their order after the sorting has been performed.
# This sort is not adaptive. Adaptive means that algo can judge itself whether the list is already sorted and then break the loop.
# No matter what the original ordering of the elements, merge sort will execute in exactly the same time, and will perform the same set of operations.


#-------------------CODE-----------------------------

def merge_sort(l):
    if len(l)>1:
        
        mid = len(l) // 2
        
        left = l[:mid]
        right = l[mid:]

        merge_sort(left)        # Using Recurrsion to split the left half further into multiple halves till it gets single element
        merge_sort(right)       # Using Recurrsion to split the right half further into multiple halves till it gets single element
       

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):     #loop till the length of both the lists
            if left[i] < right[j]:                  #If left list's first element is smaller then putting it into 0th index of original/new list
                l[k] = left[i]
            
                i = i + 1                           #Incrementing the list index since 1 elem is already gone
            else:
                l[k] = right[j]                     #If right list's first element is smaller then putting it into 0th index of original/new list  
                j = j + 1                           #Incrementing the list index since 1 elem is already gone
            k=k+1                                   #Incrementing the original/new list index since 1 elem is already inplace

#Looping till the length of an individual list if it has any extra elements because above 'while' loop will run till both the lists have same no of elements.
#There may be a scenario where 1 list would have more elements which was not covered in above loop
#Putting these extra elements at the end of original/new list and increment the counter for both list and original/new list so that whole list gets consumed
        while i < len(left):                        
            l[k] = left[i]                          
            
            i = i + 1
            k = k + 1

        while j < len(right):
            l[k] = right[j]

            j = j + 1
            k = k + 1

l = [12,3,56,6,7,81,0,1,13]
merge_sort(l)
print(l)

#--------------Insertion Sort-----------
# Insertion Sort Algorithm is quite similar to bubble sort but in this sorting,we compare element not just with an adjacent element but with all the left elements
# This is accomplished by means of pairwise comparisons of all the elements which are left to it.
# And then swapping them over if they're not in the correct order.
# Better than bubble sort with less overhead 


# Complexity = O(n**2)
# Comparisons = O(n**2) as n comparisons in 1 ieration, n-1 in 2nd , n-2 in 3rd and so on which is n(n-1)(n-2) which is ~equal to n**2
# Swaps = O(n**2) as a swap may be required at every single step of every single iteration
# Space Complexity = O(1) as  there is no extra space which is required. Sorting is inplace
# This sorting is stable as entities which are equal in value in the input array are not rearranged in the sorted array.
# Stable elements which are equal in value in the input array retain their order after the sorting has been performed.
# This sort is adaptive. Adaptive means that algo can judge itself whether the list is already sorted and then break the loop.


#-------------------CODE-----------------------------

def insertion_sort(l):
    length = len(l)
    for i in range(0, length-1):        #first loop to pick an element.Since we are taking j=i+1 so, we should run loop till 2nd last element so that j can start from last element as i+1
        for j in range(i+1,0,-1):       #Going in the direction of left hence starting from higher to lower index.j=i+1 so that for i=0; j starts from 1 not 0 otherwise no loop in 1 iteration from 0 to 0
            if l[j] < l[j-1]:           #Comparing current element from all previous elements and make swaps as required
                l[j], l[j-1] = l[j-1], l[j]
            else:
                break

    print('Sorted list: ',l)

l = [12,3,56,6,7,81,0,1,13]
insertion_sort(l)

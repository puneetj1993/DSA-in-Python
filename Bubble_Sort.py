#--------------Bubble Sort-----------
# Bubble Sort Algorithm ,the largest element bubbles over to its correct position at each iteration.
# This is accomplished by means of pairwise comparisons of adjacent elements
# And then swapping them over if they're not in the correct order. 


# Complexity = O(n**2)
# Comparisons = O(n**2) as n comparisons in 1 ieration, n-1 in 2nd , n-2 in 3rd and so on which is n(n-1)(n-2) which is ~equal to n**2
# Swaps = O(n**2) as a swap will be required at every single step of every single iteration
# Space Complexity = O(1) as  there is no extra space which is required. Sorting is inplace
# This sorting is stable as entities which are equal in value in the input array are not rearranged in the sorted array.
# Stable elements which are equal in value in the input array retain their order after the sorting has been performed.
# This sort is not really adaptive. Adaptive means that algo can judge itself whether the list is already sorted and then break the loop.
# Can be adaptive manually if we can count the no of swaps in an iteration and if it is 0 then it means sorting is completed.

#-------------------CODE-----------------------------

def bubble_sort(l):
    length = len(l)
    for i in range(0, length):
        for index in range(0,length-1-i):
            if l[index] > l[index + 1]:
                l[index + 1], l[index] = l[index], l[index + 1]

    print('Sorted list: ',l)

l = [12,3,56,6,7,81,0,1,3]
bubble_sort(l)

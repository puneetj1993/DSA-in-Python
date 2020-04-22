#--------------Selection Sort-----------
# Selection Sort Algorithm selects one element at a time and then compares it to every other element in the list.
# Out of the unsorted elements in the array, the smallest element is located in each iteration.
# And this is placed into its correct position in the sorted part of the array

# Complexity = O(n**2)
# Comparisons = O(n**2) as n comparisons in 1 ieration, n-1 in 2nd , n-2 in 3rd and so on which is n(n-1)(n-2) which is ~equal to n**2
# Swaps = O(n) as single swap operation which is performed at each iteration
# Space Complexity = O(1) as  there is no extra space which is required. Sorting is inplace
# This sorting is not stable as entities which are equal in value in the input array may in fact be rearranged in the sorted array.
# Stable elements which are equal in value in the input array retain their order after the sorting has been performed.

#-------------------CODE-----------------------------

def selection_sort(l):
    length = len(l)
    
    for i in range(length):
        min_value_index = i
        for j in range(i + 1, length):
            if l[min_value_index] > l[j]:
                min_value_index = j
        l[i], l[min_value_index] = l[min_value_index], l[i]

    print('Sorted list: ',l)

l = [12,3,56,6,7,81,0,1,3]
selection_sort(l)

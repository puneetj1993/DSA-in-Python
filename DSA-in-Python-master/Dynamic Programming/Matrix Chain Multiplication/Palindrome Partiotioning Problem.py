"""
Palindrome Partitioning using Recursion
Given a string, a partitioning of the string is a palindrome partitioning if every substring of the partition is a palindrome. Find out 
the minimum no of partitions required to get all the substrings as palindrome

I/P: A string = "aitib"
O/P: we need 2 partitions to get a, iti, b as all these are palindrome

"""
#-------------------Recursion Code---------------------
s = "aitib"
i=0
j=len(s)-1

def is_palindrome(s,i,j):
    ss = s[i:j+1]
    return ss == ss[::-1]

    
def solve(s,i,j):
    
    
    # Base condition
    if i>=j or is_palindrome(s,i,j):
        return 0
        
    min1 = 65536  # creating min1 local var here as global is giving wrong answer. This will not impact as we are returning min here
    # rather than temp_ans like in original MCM question
    
    # Loope to move k across the array
    for k in range(i,j):
        # Temp answer for each k
        temp_ans = 1 + solve(s,i,k) + solve(s,k+1,j) 
        
        # To store the minimum value as for loop proceeds
        min1 = min(min1, temp_ans)
            
    return min1

print(solve(s,i,j))

#-------------------Top Down (Memoization)---------------------

s = "nitik"
i=0
j=len(s)-1

t=[[-1 for j in range(len(s)+1)] for i in range(len(s)+1)]

def is_palindrome(s,i,j):
    ss = s[i:j+1]
    return ss == ss[::-1]

    
def solve(s,i,j):
    
    
    # Base condition
    if i>=j or is_palindrome(s,i,j):
        return 0
    
    if t[i][j]!= -1:
        return t[i][j]
        
    min1 = 65536  # creating min1 local var here as global is giving wrong answer. This will not impact as we are returning min here
    # rather than temp_ans like in original MCM question
    
    # Loope to move k across the array
    for k in range(i,j):
        # Temp answer for each k
        temp_ans = 1 + solve(s,i,k) + solve(s,k+1,j) 
        
        # To store the minimum value as for loop proceeds
        min1 = min(min1, temp_ans)
            
    t[i][j] = min1
    return t[i][j]

print(solve(s,i,j))

#-------------------Top Down (Memoization) with extra optimization---------------------

s = "nitik"
i=0
j=len(s)-1

t=[[-1 for j in range(len(s)+1)] for i in range(len(s)+1)]

def is_palindrome(s,i,j):
    ss = s[i:j+1]
    return ss == ss[::-1]

    
def solve(s,i,j):
    
    
    # Base condition
    if i>=j or is_palindrome(s,i,j):
        return 0
    
    if t[i][j]!= -1:
        return t[i][j]
        
    min1 = 65536  # creating min1 local var here as global is giving wrong answer. This will not impact as we are returning min here
    # rather than temp_ans like in original MCM question
    
    # Loope to move k across the array
    for k in range(i,j):
        
        # Here, we are checking whether call to indvidual sub problem exists in matrix
        # If yes, then directly used it otherwise, call the sub problem
        if t[i][k]!=-1:
            left = t[i][k]
        else:
            left = solve(s,i,k)
            t[i][k] = left
        
        if t[k+1][j]!=-1:
            right = t[k+1][j]
        else:
            right = solve(s,k+1,j)
            t[k+1][j] = right
         
        # Temp answer for each k
        temp_ans = 1 + left + right
        
        # To store the minimum value as for loop proceeds
        min1 = min(min1, temp_ans)
            
    t[i][j] = min1
    return t[i][j]

print(solve(s,i,j))
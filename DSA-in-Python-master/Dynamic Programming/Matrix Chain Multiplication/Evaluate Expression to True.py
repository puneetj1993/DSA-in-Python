"""
Evaluate Expression To True
Given a boolean expression with following symbols.
Symbols
    'T' --- True 
    'F' --- False 
And following operators filled between symbols
Operators
    &   --- boolean AND
    |   --- boolean OR
    ^   --- boolean XOR 
Count the number of ways we can parenthesize the expression so that the value of expression evaluates to true.
Example:
Input: symbol[]    = {T, F, T}
       operator[]  = {^, &}
Output: 2
The given expression is "T ^ F & T", it evaluates true
in two ways "((T ^ F) & T)" and "(T ^ (F & T))"
"""

s = "T|F&T^F"
i=0
j=len(s)-1
    
def solve(s,i,j, isTrue):
# Requirement of isTrue(Bool) is there because for making end exp as True there might be cases where sub problem can be false
# So, for OR case if left subproblem returns False and right one return True then also, total is True so if we don't calculate for False as well
# Then, it will only calculate the ways where both the subproblems and hence, final problem is True which is not the correct answer 
    # Base condition
    
    if i>j:
        return True
    
    if i ==j:
    # If single element is present
        if isTrue:
            return s[i]=='T'
        else:
            return s[i] == 'F'
        
    ans = 0
    
    # Loope to move k across the array
    # K will be from i+1 to j-1 so, function call will be from i to (k-1) and (k+1 to j)
    # As we will have char ,op, char ...., so every char will be at k+2th position
    # i and j represents the symbols T or F and k represents the operator 
    for k in range(i+1,j,2):
        
        """
        Here, as already mentioned we may need combination of False and True for left and right subproblem
        lt = left subproblem return True
        lf = left subproblem return False
        rt = right subproblem return True
        rf = right subproblem return False
        """
        lt = solve(s,i,k-1,True)
        lf = solve(s,i,k-1,False)
        rt = solve(s,k+1,j,True)
        rf = solve(s,k+1,j,False)
        
        # The below code represents the no of ways for each individual character
        if s[k]=='^':
            if isTrue:
                ans= ans + lt*rf + lf*rt
            else:
                ans= ans + lt*rt + lf*rf

        elif s[k]=='&':
        # Like for AND, to make it true, l and r both should be true thatswhy, ans + lt*rt
        # We used multiply insted of add as say lt =2 ways , rt=4 ways then there will be total 8 ways as lt can be clubbed with all 4 rt one by one
        # which makes 4 ways and then 4 for other lt this makes it 8 ways . If we used + then there will be only 6 ways which is not correct
            if isTrue:
                ans = ans + lt*rt;
            else:
            #Like for AND, to make it flase, l and r both should be false or atleast one of them is falsee thatswhy, ans + 3 things
            # So, this may look big and complex but this is pure maths
                ans= ans + lt*rf + lf*rt + lf*rf
                
        elif s[k]=='|':
            if isTrue:
                ans = ans + lt*rf + lf*rt + lt*rt
            else:
                ans = ans + lf*rf
    
    return ans

# As we want end result i.e. expression to be True so, we will feed True here in place of isTrue
print(solve(s,i,j,True))

#-------------Top Down Memoization------------------------

s = "T|F&T^F"
i=0
j=len(s)-1
    
def solve(s,i,j, isTrue):
# Requirement of isTrue(Bool) is there because for making end exp as True there might be cases where sub problem can be false
# So, for OR case if left subproblem returns False and right one return True then also, total is True so if we don't calculate for False as well
# Then, it will only calculate the ways where both the subproblems and hence, final problem is True which is not the correct answer 
    # Base condition
    
    if i>j:
        return True
    
    if i ==j:
    # If single element is present
        if isTrue:
            return s[i]=='T'
        else:
            return s[i] == 'F'
    
    # Adopting memoization, since 3 variables i,j,isTrue are changing so, this will create 3D DP matrix of t[len(s)+1][len(s)+1][2] as i and j = #len(s) and isTrue will have only 2 values as True or False. sometime,people may have issue with imaganing the 3D table so, we can use #dictionary as well for memoization
    # Here, to have distinct keys , we can create a temp string with i, jand isTrue like i+space+j+space+isTrue.
    # and follow the same principal that if temp string is present in dictionary then gets its value otherwise continue just like the table
    temp = str(i)+" "+str(j)+" "+str(isTrue)
    if mp.get(temp,0):
        return mp[temp]
        
    ans = 0
    
    # Loope to move k across the array
    # K will be from i+1 to j-1 so, function call will be from i to (k-1) and (k+1 to j)
    # As we will have char ,op, char ...., so every char will be at k+2th position
    # i and j represents the symbols T or F and k represents the operator 
    for k in range(i+1,j,2):
        
        """
        Here, as already mentioned we may need combination of False and True for left and right subproblem
        lt = left subproblem return True
        lf = left subproblem return False
        rt = right subproblem return True
        rf = right subproblem return False
        """
        lt = solve(s,i,k-1,True)
        lf = solve(s,i,k-1,False)
        rt = solve(s,k+1,j,True)
        rf = solve(s,k+1,j,False)
        
        # The below code represents the no of ways for each individual character
        if s[k]=='^':
            if isTrue:
                ans= ans + lt*rf + lf*rt
            else:
                ans= ans + lt*rt + lf*rf

        elif s[k]=='&':
        # Like for AND, to make it true, l and r both should be true thatswhy, ans + lt*rt
        # We used multiply insted of add as say lt =2 ways , rt=4 ways then there will be total 8 ways as lt can be clubbed with all 4 rt one by one
        # which makes 4 ways and then 4 for other lt this makes it 8 ways . If we used + then there will be only 6 ways which is not correct
            if isTrue:
                ans = ans + lt*rt;
            else:
            #Like for AND, to make it flase, l and r both should be false or atleast one of them is falsee thatswhy, ans + 3 things
            # So, this may look big and complex but this is pure maths
                ans= ans + lt*rf + lf*rt + lf*rf
                
        elif s[k]=='|':
            if isTrue:
                ans = ans + lt*rf + lf*rt + lt*rt
            else:
                ans = ans + lf*rf
    
    mp[temp] = ans
    return mp[temp]

# As we want end result i.e. expression to be True so, we will feed True here in place of isTrue
print(solve(s,i,j,True))

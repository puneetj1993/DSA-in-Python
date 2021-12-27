"""
PS:- printing the Shortest Common Supersequence
i/p: 2 strings X and Y
o/p: print shortest common supersequences string
expected o/p: "AGXGTXAXB" OR "AGGXTXAXB"
"""

x="aggtab"
y="gxtxaxb"

m=len(x)
n=len(y)
res=""
# A matrix of t[m+1][n+1] with base value of -1
t = [[-1 for j in range(n+1)] for i in range(m+1)]

# Initialization of table with base condition
for i in range(m+1):
    for j in range(n+1):
        if i==0:
            t[i][j] = 0
        if j==0:
            t[i][j] = 0

for i in range(1,m+1):
    for j in range(1,n+1):
        # Choice diagram
        if x[i-1] == y[j-1]:
            t[i][j] = 1 + t[i-1][j-1]  
        else:
            t[i][j] = max(t[i-1][j], t[i][j-1])
            
i = m
j = n
while i>0 and j>0:
    """ Here, we need to add both LCS and not equal item once"""
    if x[i-1] == y[j-1]:
        res = res + x[i-1]
        i=i-1
        j=j-1
    else:
        if t[i][j-1]>t[i-1][j]:
            res = res + y[j-1]
            j=j-1
        else:
            res = res + x[i-1]
            i=i-1

# If X reaches its end, put remaining characters 
# of Y in the result string. Suppose, X reaches end
# then in LCS, we dont add anything as LCS of 2 strings where 1 string is
# empty is empty but in supersequence, we need to add the remaining string as 
# SCS = a + b - LCS
while j>0:
    res=res+y[j-1]
    j=j-1

# If Y reaches its end, put remaining characters 
# of X in the result string
while i>0:
    res=res+x[i-1]
    i=i-1

# Answer
print(res[::-1])
"""
PS:- Longest Repeating SubSequence i.e. subsequence that it repeating
I/P: 1 string X 
O/P: Print the length of LRS
expected o/p: 1
"""

# Here only 1 string is given but for LCS we should have 2 strings
# so, we have to derive second string.
# If we take y=reverse(x) then LCS of x and y is LPS
x="AABCABB"

y = x


m=len(x)
n=len(y)

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
        if x[i-1] == y[j-1] and i!=j: #addition change i!=j
            t[i][j] = 1 + t[i-1][j-1]  
        else:
            t[i][j] = max(t[i-1][j], t[i][j-1])
            
# Answer
print(t[m][n])
"""
PS:- printing the Longest Common Subsequence
i/p: 2 strings X and Y
o/p: print longest common subsequences
expected o/p: "gtab"
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

# Start loop from t[m][n] until i/j become 0            
i = m
j  = n
while i>0 and j>0:
    # if last element is same then add it to string and move back
    if x[i-1] == y[j-1]:
        res = res + x[i-1]
        i=i-1
        j=j-1
    else:
        if t[i][j-1]>t[i-1][j]:
            j=j-1
        else:
            i=i-1

# Answer
print(res[::-1])
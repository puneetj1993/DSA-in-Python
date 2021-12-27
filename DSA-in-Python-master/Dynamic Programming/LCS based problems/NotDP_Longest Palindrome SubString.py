"""
PS:- Longest Palindrome substring
i/p: 1 strings S  ababc
o/p: length/string itself of longest palindromic substring 
expected o/p: 3 (aba or bab)
"""

s="ababc"
n = len(s)

#string counters
L = R = 0

# For odd case
for i in range(n):
    l = r = i
    while l >= 0 and r < n and s[l] == s[r]:
        l -= 1
        r += 1
    if r - l - 1 > R - L + 1:
        L, R = l + 1, r - 1

# for even case        
for i in range(n - 1):
    l, r = i, i + 1
    while l >= 0 and r < n and s[l] == s[r]:
        l -= 1
        r += 1
    if r - l - 1 > R - L + 1:
        L, R = l + 1, r - 1
        
print(s[L:R + 1])
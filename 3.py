# A furnishing company is manufacturing a new collection of curtains. The curtains are of two colors aqua(a) and black (b).
# The curtains color is represented as a string(str) consisting of a’s and b’s of length N.
# Then, they are packed (substring) into L number of curtains in each box. 
# The box with the maximum number of ‘aqua’ (a) color curtains is labeled. The task here is to find the number of ‘aqua’ color curtains in the labeled box.

# Example 1:

# Input :

# bbbaaababa -> Value of str

# 3    -> Value of L

# Output:

# 3   -> Maximum number of a’s

import sys

def maxAqua(s:str,L:int)-> int:
    max_count = 0
    current_count = 0
    
    #Sliding window approach
    
    #Count a in first window
    for i in range(L):
        if s[i] == 'a':
            current_count = current_count + 1
            
    for i in range(L,len(s)):
        if s[i-L] == 'a':
            current_count = current_count - 1
        if s[i] == 'a':
            current_count = current_count + 1
        max_count = max(max_count,current_count)
    return max_count

data  = sys.stdin.readline().split()
s = data[0] # First input 
L = int(data[1]) # Second input
print(s)
print(L)
result = maxAqua(s,L)
print(result)

# Input : 7
# Output : 101 102 101 103 101 102 104

import sys
data = sys.stdin.readline().strip()
n = int(data[0])

arr = list(map(int,sys.stdin.readline().strip().split()))



freq = {}

for movie_id in arr:
    if movie_id in freq:
        freq[movie_id] +=1
    else:
        freq[movie_id] = 1
        
for movie_id in sorted(freq.keys()):
    print(movie_id, freq[movie_id])
    
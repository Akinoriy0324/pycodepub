import sys
import re
sys.setrecursionlimit(100000)

n = int(input())
tmp = str(input())
st  = re.sub('[bfghijklmnpqsuvwxyz]','',tmp)
n = len(st)
DP =  [[0]*8 for i in range(n+1)]
DP[0][0]=1

M = 10**9 + 7

cnt=0

if n<=6 :
    print(cnt)
    exit(0)

for i in range(1,n+1) :
    for j in range(0,8):
        if j < 7 and st[i-1] == "atcoder"[j]  :
            DP[i][j+1] += DP[i-1][j]  
            DP[i][j+1] %= M  
            
        DP[i][j] += DP[i-1][j]
        DP[i][j] %= M
        ##print("DP[{}][{}]={}".format(i,j,DP[i][j]) )

print( DP[n][7] % M )

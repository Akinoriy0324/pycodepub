import itertools
import math
import collections
deb = 0
n = int(input())

lis = list(map(int,input().split()))
lis.insert(0,0)
ans = 0 
MOD = 998244353

for i in range (1,n+1) :
    modlis = list(map(lambda x: x % i, lis))
    if deb : print (modlis)
    m = collections.Counter(modlis)
    ##print("modlis: ", modlis)
    MAP = [[[0] * i for k in range(n+1)] for j in range(n+1)]
    MAP[0][0][0] = 1
    for j in range(0,n) :
        for k in range (0, j+1) :
            for l in range (0,i) :
                MAP[j+1][k][l] += ( MAP[j][k][l] % MOD )
                z = l + modlis[j+1]
                if z >= l : z -= i  
                MAP[j+1][k+1][z] += ( MAP[j][k][l] % MOD )
    ans += MAP[n][i][0] 
    ans %= MOD 
    if deb :
        for data in MAP :print (data)

print (ans)


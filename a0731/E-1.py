import sys
##sys.setrecursionlimit(100000)

import itertools
import math
import collections
deb = 0

n, e, k = map(int,input().split())
#MAP = [[] for j in range(n+1)]
#ED = [[] for j in range(e)]
degs = [0 for j in range(n+1)]
for i in range(0,e) :
    a, b =  map(int,input().split())
    #MAP[a].append(b)
    degs[a] += 1
    #MAP[b].append(a)
    degs[b] += 1
    #ED[i] = [a,b]
ans = 0 
MOD = 998244353

MAX = 2*(10**5) + 1  # n の取りうる最大値( ただし, MODより小さいものとする )を取る

fac = [1] + [1]
finv = [1] + [1]
inv = [0] + [1]

for i in range(2, MAX):
    fac += [fac[-1] * i % MOD]
    inv += [MOD - inv[MOD%i] * (MOD // i) %MOD]
    finv += [finv[-1] * inv[i] % MOD]


def comb(n, k):
    if n < 0 or k < 0 or n < k:
        return 0
    return fac[n] * finv[k] * finv[n-k] % MOD

oddcnt = 0 
for i in range(1,n+1) : 
    if degs[i] % 2 == 1 : oddcnt += 1

for i in range(0,k+1,2) :
    # if i % 2 == 1 : continue
    ans += comb(oddcnt,i) * comb(n-oddcnt,k-i)    
    ans %= MOD

print(ans)

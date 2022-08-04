import sys
sys.setrecursionlimit(100000)

n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

sortA = sorted(A)
sortB = sorted(B)

res = 10**10
tmp = 0
for i in range(0,n)  :
    tmp += abs (sortA[i] - sortB[i])

print(tmp)

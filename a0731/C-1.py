n = int(input())
MAP = [[] for j in range(n+1)]

lis = list(map(int,input().split()))
lis.insert(0,0)

##print(lis)
cnt1 = 0
cnt2 = 0
for i in range(1,n+1) :
    if lis[i] == i :
        cnt1 += 1
    else :
        if lis[lis[i]] == i :
            cnt2 += 1 

if cnt1 == 0 : cnt1 = 1

print(int (cnt1*(cnt1-1)/2 + cnt2/2) )

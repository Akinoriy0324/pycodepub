import sys
import collections
import time
sys.setrecursionlimit(200000)
start = time.time()
deb = 0

n , k = map(int,input().split())
MAP = [[] for j in range(n+1)]
MAPB = [[] for j in range(n+1)]

for i in range(1,k+1):
    a, b = map(int, input().split())
    MAP[a].append(b) 
    MAPB[b].append(a)


## 強連結分解 ## 

def dfsbefore():
    CON = [ 0 for j in range(n+1)]
    order = []  
    #[ -1 for j in range(n+1)]
    checked = [ -1 for j in range(n+1)]
    ord = n-1
    for i in range(1, n+1) :
        if CON[i]==0 :
            Q = collections.deque()
            Q.append(i)

            while Q :
                now = Q[-1]
                #print ("Now", now)
                if CON[now] == 0 :
                    CON[now] = 1 
                    for to in reversed(MAP[now]):
                        if CON[to] == 0 : 
                            Q.append(to)
                            #print (now , "append", to)
                elif CON[now] == 1 :                    
                    CON[now] = 2
                    order.append(now)
                    ##order[ord] = now 
                    ord -= 1
                    Q.pop()
                else :
                    Q.pop()
    r_order = list(reversed(order))
    return r_order

def dfsafter(lis):
    CON = [ 0 for j in range(n+1)]
    checked = [ -1 for j in range(n+1)]
    res = []    
    tmp = []
    for i in lis :
        if len(tmp) > 0 : 
            res.append(tmp)
            tmp = []
        if CON[i]==0 : 
            Q = collections.deque()
            Q.append(i)

            while Q :
                now = Q[-1]
                if CON[now] == 0 :
                    CON[now] = 1 
                    for to in reversed(MAPB[now]):
                        if CON[to] == 0 : 
                            Q.append(to)
                            #print (now , "append", to)
                elif CON[now] == 1 :                    
                    CON[now] = 2
                    tmp.append(now)
                    Q.pop()
                else :
                    Q.pop()

    if len(tmp) > 0 : 
        res.append(tmp)
        tmp = []
    #for dat in res : print(len(res))
    return res

def main() :
    ans = 0
    
    beforeans = dfsbefore()
    #print( beforeans)
    #print(time.time()-start )        

    afterans = dfsafter(beforeans)
    #print(afterans)
    for dat in afterans :
        if len(dat)>=2 :
            ans += len(dat) * (len(dat) - 1) // 2
    print(ans)
    #print(time.time()-start )        
main()

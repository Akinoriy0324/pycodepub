import sys
import collections
import math
sys.setrecursionlimit(50000)

n = int(input())
MAP = [[] for j in range(n+1) ]
for i in range(1,n) :
    a , b = map(int,input().split())
    MAP[a].append(b)
    MAP[b].append(a)
    
def dfs():
    CON = [ 0 for j in range(n+1)]
    color = [ -1 for j in range(n+1)]  
    for i in range(1, n+1) :
        if CON[i]==0 :
            Q = collections.deque()
            Q.append(i)
            color[i]=1
            while Q :
                now = Q[-1]
                if CON[now] == 0 :
                    CON[now] = 1 
                    for to in reversed(MAP[now]):
                        if CON[to] == 0 : 
                            Q.append(to)
                            color[to] = (color[now] +1)%2
                elif CON[now] == 1 :                    
                    CON[now] = 2
                    Q.pop()
                else :
                    Q.pop()
    ##print(color)
    return color

def main() : 
    color = dfs()
    if color.count(0) >= n//2 :
        p = 0
    else : 
        p = 1  
    prtcnt = 0 
    for i in range(1,n+1) :
        if color[i] == -1 : continue 
        if color[i] == p and prtcnt < n/2: 
            prtcnt += 1
            print ( i, end='')
            if prtcnt == n//2 :
                print ('')
            else :
                print (' ', end='')

        
main()
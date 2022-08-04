import sys
from collections import deque
sys.setrecursionlimit(50000)
deb = 0

H, W=  map(int, input().split()) 
n = int(input())
MAP = [[0 for i in range(W+2)] for j in range(H+2)]
PAR  = [[None for i in range(W+2)] for j in range(H+2)]
RANK = [[0 for i in range(W+2)] for j in range(H+2)]
# print(MAP)

def main() :
    for i in range(0,n) :
        temp = list(map(int, input().split()))
        if temp[0] == 1 :
            x1 = temp[1]
            y1 = temp[2]
            if deb : print ("ins",x1, y1)
            #MAP[x1][y1] = 1
            ins(x1,y1)            
        else :
            x1 = temp[1]
            y1 = temp[2]
            x2 = temp[3]
            y2 = temp[4]
            if deb: print ("check",x1,y1,x2,y2)
            #print(x1,y1,'>>',x2,y2)
            #for m in MAP[1:] : 
            #    print(m) 
            parch1 = parcheck(x1,y1)
            if parch1 != None :
                parch2 = parcheck(x2,y2)
                if parch2 != None and parch1 == parch2 : 
                    print("Yes")
                else : 
                    print("No")
            else : 
                print("No")

def parcheck(x1,y1) :
    p = PAR[x1][y1] 
    x = None
    y = None
    while p != None and p !=[x,y]:
        x , y = p
        p = PAR[x][y]
    
    if x == None : 
        if deb : print ("par",x1,y1,"is None" )        
        return None
    else : 
        if deb : print ("par",x1,y1,"is",x,y)
        return [x, y]

def unite(x1,y1,x2,y2) :
    # どっちを親にするかを考える。
    px1,py1 = parcheck(x1,y1)
    px2,py2 = parcheck(x2,y2)
    if RANK[px1][py1] > RANK[px2][py2] :
        PAR[px2][py2] = [px1,py1] 
    elif RANK[px1][py1] < RANK[px2][py2] :
        PAR[px1][py1] = [px2,py2]
    else : 
        PAR[px2][py2] = [px1,py1] 
        RANK[px1][py1] += 1
    return 


def ins(x,y) :
    MAP[x][y] = 1
    PAR[x][y] = [x,y]

    if MAP[x+1][y]==1 :
        unite(x+1,y,x,y)
    if MAP[x][y+1] == 1 :
        unite(x,y+1,x,y)
    if MAP[x-1][y] ==1  :              
        unite(x-1,y,x,y)
    if MAP[x][y-1] ==1 :
        unite(x,y-1,x,y)

    if deb : 
        for a in MAP: print(a)
    if deb : 
        for p in PAR: print(p)


main()

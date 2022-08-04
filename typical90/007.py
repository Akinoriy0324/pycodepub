import sys
sys.setrecursionlimit(100000)

n = int(input())
i = 0 
while True :
	if (2**i >= n) :
		break
	i += 1

#  1-index
N = 2**(i+1) 

TR1 = [0]*N
TR2 = [0]*N

A = []
A.insert(0, [0,0])

for i in range (1,n+1) :
	a = list(map(int,input().split())) 
	A.append(a)	
	if A[i][0] ==1 :
		TR1[i+ int(N/2) -1] += A[i][1]
	else :
		TR2[i+ int(N/2) -1] += A[i][1]


for i in range(int(N/2)-1 , 0 , -1) :	
	TR1[i] = TR1[i*2] + TR1[i*2+1]
	TR2[i] = TR2[i*2] + TR2[i*2+1]

q = int(input())

#print(A)
#print(TR1)
#print(TR2)

def solve (beg,end,lt,rt,num) :
	#print("{} {} {} {} {}",beg,end,lt,rt,num)
	if rt - lt < 1 : 
		#print("PA1")
		return [0, 0]
	if rt <= beg or end <= lt :
		#print("PA2")
		return [0, 0] 
	if beg <= lt and rt <= end : 
		#print("PA3")
		return [TR1[num], TR2[num]]
	mid = int((lt+rt)/2 )
	return [x + y for (x, y) in zip(solve(beg,end,lt,mid,2*num), solve(beg,end,mid,rt,2*num+1))]

"""
def solve1 (beg,end,lt,rt,num) :
	#print("{} {} {} {} {}",beg,end,lt,rt,num)
	if rt - lt < 1 : 
		#print("PA1")
		return 0
	if rt <= beg or end <= lt :
		#print("PA2")
		return 0 
	if beg <= lt and rt <= end : 
		#print("PA3")
		return TR1[num]
	mid = int((lt+rt)/2 )
	return solve1(beg,end,lt,mid,2*num) + solve1(beg,end,mid,rt,2*num+1)
 
def solve2 (beg,end,lt,rt,num) :
	print("{} {} {} {} {}",beg,end,lt,rt,num)
	if rt - lt < 1 : 
		#print("PA1")
		return 0
	if rt <= beg or end <= lt :
		#print("PA2")
		return 0 
	if beg <= lt and rt <= end : 
		#print("PA3")
		return TR2[num]
	mid = int((lt+rt)/2 )
	return solve2(beg,end,lt,mid,2*num) + solve2(beg,end,mid,rt,2*num+1)
 		
"""

for i in range (0,q) :
    sum1 = 0
    sum2 = 0
    beg , end = list(map(int,input().split()))
    # print (solve1(beg,end +1,1,int(N/2)+1,1),solve2(beg,end +1,1,int(N/2)+1,1))
    res = solve(beg,end +1,1,int(N/2)+1,1)
    print (res[0],res[1])
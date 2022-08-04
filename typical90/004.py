H, W = list(map(int,input().split())) 
A = []

COL = [0]*W
ROW = [0]*H


for i in range(0, H) :
	a = list (map(int,input().split()))
	##print(a)
	A.append(a)
	ROW[i] = sum(a)

for j in range(0,W) :
	for i in range(0,H) :
		COL[j] += A[i][j]  

              
for i in range (0,H) :
	for j in range(0,W) :
		print ( ROW[i] + COL[j] - A[i][j],end='')
		if j < W -1  : print(" ",end='')
		else : print("")


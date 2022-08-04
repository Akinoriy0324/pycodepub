import sys
sys.setrecursionlimit(75000)
###binary search###

n, l = list(map(int,input().split()))
k = int(input())
lines = list(map(int,input().split()))
lines = [0] + lines

def solve(left,right) :
	##print("left: " + str(left) +"right: " + str(right) )
	res = 0
	if right - left == 1 :
		res = left
	else:
		mid = int( (left + right) / 2 )
       	#mid以上の解があるかを検索する
        #言い換えるとmid未満のピースがないということ
		if judge(mid) :
			res = solve(mid,right)
		else : 
			res = solve(left,mid)
	return res

def judge (mid):
	##print("mid : " + str(mid) )
	left = 0
	cut = 0
	for line in lines :
		if line - left >= mid and l - line >= mid :
			left = line
			cut += 1
		if (cut >= k) : break

	if (cut == k) :
		return True
	else:
		return False
       
print(solve(0,l+1))
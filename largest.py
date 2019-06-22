n=int(input())
l=list(map(int,input().split()))
a=0
l.sort()
for i in range(n-1,-1,-1):
	a=a*10+l[i]
print(a)
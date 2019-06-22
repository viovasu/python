n=int(input())
l=list(map(int,input().split()))
s=[]
for i in range(0,n):
	if l[i]%2==0:
		if i%2==1:
			s.append(l[i])
			i=i+1
	elif l[i]%2==1:
		if i%2==0:
			s.append(l[i])
			i=i+1
for i in s:
	print(i,end=" ")
n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(0,n):
	for j in range(i+1,len(l)):
		if l[j]==l[i]:
			a.append(l[i])
if(len(a)==0):
	print("unique")
else:
	a.sort()
	b=a
	for i in b:
		print(i,end=" ")
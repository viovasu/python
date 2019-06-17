a,b=map(int,input().split())
for i in range(a+1,b):
	x=0
	p=i
	while(p>0):
		c=p%10
		p=p//10
		y=c**3
		x=x+y
	if(i==x):
		print(x,end=' ')
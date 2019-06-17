n=int(input())
m=str(n)
k=len(m)
s=0
z=n
while(n!=0):
	r=n%10
	s=s+r**k
	n=n//10
if z==s:
	print("yes")
else:
	print("no")
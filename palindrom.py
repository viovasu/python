n=int(input())
m=0
p=n
while(n!=0):
	r=n%10
	m=(m*10)+r
	n=n//10
if m==p:
	print("yes")
else:
	print("no")
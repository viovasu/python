a=int(input())
b=int(input())
sum=0
c=list(map(int,input().split()))
for i in range(0,b):
	sum=sum+c[i]
print(sum)
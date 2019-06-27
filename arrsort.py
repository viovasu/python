n=int(input())
l=list(map(int,input().split()))
l.sort()
for i in range(len(l)):
    print(l[i],end=" ")

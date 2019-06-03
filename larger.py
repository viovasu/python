n=input()
a=n.split(" ")
if (int(a[0]) > int(a[1])):
    if(int(a[0]) > int(a[2])):
        print(a[0])
    else:
        print(a[2])
elif (int(a[1]) > int(a[2])):
        print(a[1])
else:
    print(a[2])
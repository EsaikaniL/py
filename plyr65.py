n=int(input("enter the elements:"))
l=list(map(int,input().split(' ')))
s=[]
for i in l:
    if i<n:
        s.append(i)
print(*sorted(s))

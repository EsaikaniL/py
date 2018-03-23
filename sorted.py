t =[str(t) for t in input("enter the array:").split()]
if (sorted(t)==t):
    print(t,"\nthe list is already sorted")
else:
    print("no, the list is not sorted")
    t.sort()
    print(t,"is the sorted list")


n=[int(x) for x in input("enter the elements by giving whitespaces:").split()]
n.sort()
print(n)
m=int(input("enter the element to check the occurrence:"))
print(m,"is the num you wanted to check")
if m in n:
    print("yes, the given num is in the list")
else:
    print("no, the given num is not in the list.")
total = 1
n=[int(n) for n in input("enter the elements with whitespaces:").split()]
for i in range(0, len(n)):
    total *= n[i]
print (total)
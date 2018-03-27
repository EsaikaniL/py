a=[int(x) for x in input("enter the list").split()]
b=[int(y) for y in input("enter the list").split()]
print(sorted(a),"-sorted list a ", sorted(b),"-sorted list b")
if  list(set(b).intersection(a)) :
    print("yes,",list(set(b).intersection(a))," is/are common number in the sentence")
else:
     print("no , there are no nums in common", )

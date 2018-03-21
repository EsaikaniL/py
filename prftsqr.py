m=int(input("enter the range of list:"))
o=int(input("enter the range upto:"))
n = [x for x in range(m,o) if int(x**0.5) == x**0.5]
print("interval is btwn",m , "and" ,o )
print(n,"is/are the perfect square of the given interval")

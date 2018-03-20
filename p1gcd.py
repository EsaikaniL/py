def multiple(a,b):
    if(b==0):
        return a
    else:
        return multiple(b,a%b)
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
cfact = multiple(a,b)
print("common factor is:",cfact)

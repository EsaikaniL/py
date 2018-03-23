num=int(input("Enter any number"))
ans=""
for x in range(2,num):
	if num%x==0:
		num=num//x
		if x%2!=0:
			ans=ans+" "+str(x)
			print("the odd factors are:",ans)
		else:
		    print("there is no odd factor for the num")

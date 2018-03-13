string=input("Enter string:")
countnum=0
for i in string:
      if(i.isdigit()):
            countnum=countnum+1
print("The number of digits is:",countnum)

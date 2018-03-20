text=input("enter the sentence:")
ans=""
prev=" "
for i in text :
    if not (prev==" " and i==prev ):
        ans+=i
    prev=i
print(ans)
t =input("enter the sentance")
b=input("enter the char/word to be found:")
if b in t:
    print("yes",b,("is found in"),t)
else:
    print(b,"is not found in",t)

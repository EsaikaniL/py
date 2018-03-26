a=input("enter the string")
char=input("enter the char to be found:")
print(a,("is the word you entered."), ("\n"),char,("is the char u wanted to find."))
if char in a :
    print(a.index(char),("is the index of the char u entered."))
else:
    print("no, the char is not in the word ")

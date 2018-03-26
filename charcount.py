a=input("enter the string")
char=input("enter the char to be found:")
print(a,("is the word you entered."), ("\n"),char,("is the char u wanted to count."))
if char in a :
    print(a.count(char),("times  the char u entered is repeated."))
else:
    print("no, the char is not in the word ")

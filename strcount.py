a=input("enter a sentence")
char=input("enter the string to be found:")
print(a,("is the word you entered."), ("\n"),char,("is the string u wanted to count."))
if char in a :
    print(a.count(char),("times  the string u entered is repeated."))
else:
    print("no, the string is not in the word ")

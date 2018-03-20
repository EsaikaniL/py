def conso(text):
        for i in "aeiouAEIOU":
            text = text.replace(i,"")
        return text
print(conso(input("enter the text:")))
print(text[::-1])

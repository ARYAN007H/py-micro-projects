# wap to convert a no entered by the user into ots coressponding words
w = int(input("Enter the roll no:"))
num= str(w)
d = {1:"One ", 2:"Two", 3:"Three", 4:"Four", 5:"Five ", 6:"Six ", 7:"Seven ", 8:"Eight ", 9:"Nine", 0:"Zero "}
s =""
for i in num:
    s+=d[int(i)]
print(s)
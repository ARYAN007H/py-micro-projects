# wap to find no of characters and how many time they repeat 
s = input("Enter a string:")
d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i,j in d.items():
    print(i, "\t", j)
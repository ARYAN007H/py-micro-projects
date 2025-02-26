l = []
found = False
num = int(input("How many no u want to add in list?"))
for i in range(num):
    print("element no", i + 1 , end=':')
    e = int(input())
    l.append(e)
print()
print("original list:", l)
print()

#for search
try:
    s = int(input("Enter element you wanna search ?"))
    pos = 0
    for i in l:
        if i == s:
            found = True
            print("Element found at", pos)
    pos += 1
except:
    if found != True:
        print("Element not found")
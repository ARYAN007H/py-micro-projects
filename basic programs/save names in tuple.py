n =  int(input("how many names u wanna enter:"))

names = ()

for i in range(n):
    print("Enter name", i+1 , end = ':')
    n = input()
    names +=(n,)
print (names)
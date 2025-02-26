l = [6, 12,  18, 24, 30]
for i in range(len(l)):
    for j in range(1, i%4):
        print(j, "#", end=" ")
    print()
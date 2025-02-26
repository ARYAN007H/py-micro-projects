d = {}
i = 1

def add(d, i):
    try:
        a = int(input("how many keys u waana insert:"))
        while i<=a:
            key = input("ENter key :")
            value = input("Enter vaue:")
            d[key] = value
            i+=1
    except ValueError:
        print("some error occured")

add(d, i)













print(d)


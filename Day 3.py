def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y 

def divide(x, y):
    try:
        return x / y

    except ZeroDivisionError:
        return "Error! , zero se divide kyu karna hai tujhe chor"

def calculate():
    try:

        a = float(input("Enter the first number:"))
        z = input("Enter operator(+,-,*,/):")
        b = float(input("Enter the second number:"))

        if z == '+':
            result = add(a, b)
        elif z == '-':
            result  = subtract(a, b)
        elif z == '*':
            result = multiply(a, b)
        elif z == '/':
            result = divide(a, b)
        else:
            result = "andha hai kya sahi operator daal!"

        print(f"Result: {result}")

    except ValueError:
        print("Error! ;Sahi no input kar")

def main():
    while True:
        calculate()
        again = input("Dobara calculate krna hai? (ha/nhi):").lower()
        
        if again != 'ha':
            print("byem")
            break

if __name__ == "__main__":
    main()    


# before 

# a = float(input("Enter first no:"))
# c = input("Enter operator:")
# b = float(input("Enter second no:"))

# if c =='+':
#     print(a+b)
# elif c == '-':
#     print(a-b)
# elif c == '*':
#     print(a*b)
# elif c == '/':
#     print(a/b)
# else:
#     print("Invalid input")
#input any name and find if its a palindrome or not

names = input("Enter names separated by commas: ").split(',')


for name in names:
    name = name.strip()  
    if name.lower() == name[::-1].lower():  
        print(f"{name} is a palindrome")
    else:
        print(f"{name} is not a palindrome")

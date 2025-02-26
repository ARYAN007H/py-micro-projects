sentence = input("Enter sentence")
lowercase_count=uppercase_count = 0
for i in sentence:
    if i.islower():
        lowercase_count+=1
    if i.isupper():
        uppercase_count+=1

print(f"THE no of lower case letter is :{lowercase_count}"",and ""no of upper case :", uppercase_count)


#second method

# for i in sentence:
#     if i>='A' and i<='Z':
#         uppercase_count+=1
#     if i>='a' and i<='z':
#         lowercase_count+=1

# print("Number of upper case :",uppercase_count)
# print("Number of lower case :",lowercase_count)
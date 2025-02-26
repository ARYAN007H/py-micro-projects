'''INPUT ANY SENTENCE .  W.A.P TO FIND NO OF ALPHABETS, DIGITS, SPACES ETC.'''

sentence = input("Enter sentence")
alphacount=digitcount=spacecount=symbolcount=0
for i in sentence:
    if i.isalpha():
        alphacount+=1
    elif i.isdigit():
        digitcount+=1
    elif i.isspace():
        spacecount+=1
    else:
        symbolcount+=1

print("NO of alphabet", alphacount)
print("No of space", spacecount)
print("No of digit", digitcount)
print("No of symbol", symbolcount)

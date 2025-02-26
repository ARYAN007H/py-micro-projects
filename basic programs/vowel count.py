sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
vowel_count=consonant_count = 0
for i in sentence:
    if i.isalpha():
        if i in vowels:
            vowel_count += 1
        else :
            consonant_count+=1
    else:
        print("incorrect input format")
print(f"The number of vowels in the sentence is: {vowel_count,consonant_count}")

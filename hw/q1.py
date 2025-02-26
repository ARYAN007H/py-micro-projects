#QS:W.A.P to input a string from the user and do the following (seprrately).
# (1): Replace all the vowels with "x".
# (2): Reverse the order of the string.
# (3): Find the no of words in a sentence.
# (4): Count the number of words starting with "s", irrespective of case.


string = input("Enter a string:")
sentence = input("Enter a sentence : ")
def replace_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(string)):
        if string[i].lower() in vowels:
            string = string[:i] + 'x' + string[i+1:]
    return string
    


def reverse_string(string):
    return string[::-1]

def count_words(sentence):
    words = sentence.split()
    return len(words)

def count_starting_s(sentence):
    words = sentence.split()
    count = 0
    for word in words:
        if word.lower().startswith('s'):
            count += 1


replace_vowels(string)
print("Modified string: ", string)

reversed_string = reverse_string(string)
print("Reversed string: ", reversed_string)

word_count = count_words(sentence)
print("Number of words in the sentence: ", word_count)

word_count_starting_s = count_starting_s(sentence)
print("Number of words starting with 's': ", word_count_starting_s)


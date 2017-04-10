
dictionary = open("dict.txt","r")
word_list = []
for line in dictionary:
    word_list.append(line.strip())
dictionary.close()

def is_word(word):
    if word in word_list:
        return True
    else:
        return False

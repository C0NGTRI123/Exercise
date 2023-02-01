def loadfile(file):
    word_list = []
    with open(file, 'r') as f:
        data = f.readlines()
        for word in data:
            word = word.replace("\n", "")
            if len(word) > 3:
                word_list.append(word)
    return word_list

def shortestChain(word1, word2):
    res = []
    res = res + [word1]
    if start_word[-2:] == end_word[:2]:
        return chain
    for word in loadfile('wordsEn.txt'):


# print(loadfile('wordsEn.txt'))
word1 = input("Please enter the start word: ")
word2 = input("Please enter the goal word: ")
print("the shortest chain is: ")



            
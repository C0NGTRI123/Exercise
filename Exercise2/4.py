import re

with open('story.txt', 'r') as f:
    new_list = []
    data = f.readlines()
    for word in data:
        word = re.sub(r"[^a-zA-Z0-9\s]+", "", word)
        word = word.strip().split()
        for i in word:
            if len(i)!=0:
                new_list.append(i)

word_count = {}
for word in new_list:
    word_count[word] = word_count.get(word, 0) + 1
sorted_word = sorted(word_count.items(), key=lambda x:x[1], reverse=True)
for i in sorted_word[:100]:
    print(i[0], i[1])

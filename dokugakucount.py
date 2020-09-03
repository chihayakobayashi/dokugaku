word = input("type the word")

dict = dict()
for w in word:
    if w in dict:
        dict[w] += 1
    else:
        dict[w] = 1

print(dict)

from collections import Counter
print(Counter(word))


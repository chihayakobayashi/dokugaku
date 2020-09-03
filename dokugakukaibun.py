#ほくのこたえ
word = input("回文かどうか調べます")

class Stack:
    def __init__(self):
        self.items = []

    def push(self,w):
        self.items.append(w)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def confirm(word):
    stack = Stack()

    for w in word:
        stack.push(w)

    reverse = ""
    length = stack.size()

    for i in range (length):
        w = stack.pop()
        reverse += w

    if reverse == word:
        return True
    else:
        return False

answer = confirm(word)
print(answer)

#模範解答
word2 = input("回文かどうか調べます")

def palindrome(word):
    word = word.lower()
    return word[::-1] == word

print(palindrome(word2))

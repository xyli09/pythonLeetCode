
from collections import defaultdict

root = defaultdict()
endOfWord = "#"
def insert(words):
    node = root
    for char in words:
        print(char)
        node = node.setdefault(char,{})
    node[endOfWord] = endOfWord


def search(words):
    node = root
    for char in words:
        if char not in node:
            return False
        node = node[char]
    if endOfWord in node:
        return endOfWord
    else:
        return False
def startWith(prefix):
    node = root
    for char in prefix:
        if char not in node:
            return False
        node = node[char]
    return True

insert("this")
insert("word1")
insert("what")
print(root)
print(search("word"))
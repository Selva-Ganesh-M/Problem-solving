class Node:
  def __init__(self):
    self.children = [None]*26;
    self.isWord = False;


class Trie:
  def __init__(self):
    self.root = Node();

  def __getIndex(self, letter):
    return ord(letter) - ord("a");
  
  def __insert(self, word):
    crawler = self.root;
    for level in range(len(word)):
      index = self.__getIndex(word[level]);
      if not crawler.children[index]:
        crawler.children[index] = Node();
      crawler = crawler.children[index];
    crawler.isWord = True;

  def search(self, word):
    crawler = self.root;
    for level in range(len(word)):
      index = self.__getIndex(word[level]);
      if not crawler.children[index]: return;
      crawler = crawler.children[index];
    return crawler.isWord;

  def fill(self, arr):
    for word in arr: self.__insert(word);

trie = Trie();

# words = ["the"];
# src = "the";

n = input();
words = [word for word in input().split()];
src = input();
trie.fill(words)
print(1 if trie.search(src) else 0)

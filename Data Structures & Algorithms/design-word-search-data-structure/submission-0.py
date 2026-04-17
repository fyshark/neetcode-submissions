class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if cur.children[i] is None:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return node.is_end
            
            c = word[index]
            if c == ".":
                for child in node.children:
                    if child and dfs(child, index+1):
                        return True
                return False
            else:
                i = ord(c) - ord('a')
                if node.children[i] is None:
                    return False
                return dfs(node.children[i], index+1)
        return dfs(self.root, 0)

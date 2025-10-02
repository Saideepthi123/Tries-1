class Trie(object):

    class TrieNode():
        def __init__(self):
            self.children = [None] * 26
            self.isEnd = False
            self.prefix_count = 0   # number of words passing through this node
            self.end_count = 0      # number of words ending at this node

    def __init__(self):
        self.root = self.TrieNode()
        
    def insert(self, word):
        curr = self.root
        for w in word:
            idx = ord(w) - ord('a')
            if curr.children[idx] is None:
                curr.children[idx] = self.TrieNode()
            curr = curr.children[idx]
            curr.prefix_count += 1  # update prefix count
        curr.isEnd = True
        curr.end_count += 1         # update word ending count
        

    def countWordsEqualTo(self, word):
        curr = self.root
        for w in word:
            idx = ord(w) - ord('a')
            if curr.children[idx] is None:
                return 0
            curr = curr.children[idx]
        return curr.end_count


    def countWordsStartingWith(self, prefix):
        curr = self.root
        for w in prefix:
            idx = ord(w) - ord('a')
            if curr.children[idx] is None:
                return 0
            curr = curr.children[idx]
        return curr.prefix_count
        

    def erase(self, word):
        curr = self.root
        for w in word:
            idx = ord(w) - ord('a')
            if curr.children[idx] is None:
                return  # word doesn't exist
            curr = curr.children[idx]
            curr.prefix_count -= 1
        curr.end_count -= 1
        if curr.end_count == 0:
            curr.isEnd = False

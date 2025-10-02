class Solution(object):
    # tc : O(n*2) n is the len of the string 
    # sc : O(n*2) svaes all the distinct strings in it 
    class TrieNode:
        def __init__(self):
            self.children = [None]*26
    
    def __init__(self):
        self.root = self.TrieNode()

    def insert (self,word):
        node = self.root
        count = 0

        for w in word:
            idx = ord(w) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = self.TrieNode()
                count+=1
            
            node = node.children[idx]

        return count

    def countDistinct(self, s):
        count = 0
        for i in range(len(s)):
            substr = s[i:] # O(n) for each substr
            # create the tree 
            count += self.insert(substr) # O(n) for each substr 
        
        return count

        
        
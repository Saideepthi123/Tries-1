class Solution:
    # tc : insert O(n*l), dfs searrch also worst case  O(n*l) total 2*O(n*l)
    # sc : O(n*l) taken to crete the trie , O(l) for recrussion stack, O(l) for creatign the path as well total O(n*l) 
    # ran successful on leetcode

    class TrieNode:
        def __init__(self):
            self.children = [None]*26
            self.isEnd = False
            self.val = None

    def __init__(self):
        self.root = self.TrieNode()
        self.longWord = ""

    def insert(self,word):
        node = self.root

        for w in word:
            idx = ord(w) - ord('a')

            if node.children[idx] is None:
                node.children[idx] = self.TrieNode()
                node.val = w

            node = node.children[idx]
        
        node.isEnd = True
            
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # first construct the trie for the words
        for word in words: # O(n.l) where n is the number of words, l is the avergae len of these words 
            self.insert(word)

        # perform dfs and keep finding the word where every letter of it also has isend true and update the path only if the len of the word is greater than the current path

        self.dfs(self.root,[])

        return self.longWord
    
    def dfs(self,node, path):
        if len(self.longWord) < len(path):
            self.longWord = "".join(path) 

        for i in range(26): 
            if node.children[i] is not None and node.children[i].isEnd :
                # first find the letter from the i
                letter = chr(i + ord('a')) 

                # action
                path.append(letter)

                # recurse 
                # check this child node, children to find the word 
                self.dfs(node.children[i], path)

                # backtrack
                # once this path is explored we check the neighbor words 
                # so for that we should first undo adding this node and then go back to the previous path formed adn continue the recrussion

                path.pop()



    
            

    
        

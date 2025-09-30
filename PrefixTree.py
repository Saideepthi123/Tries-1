class Trie(object):
    # tc : insert, search, prefix - O(L) where L is the len of the word or prefix
    # sc : O(n*l) where n is the number of words and l is the average leng of the words,
    # creating a trie where the childen are 26 for 26 alphabets, given only for lowercase letters so 26 is fine
    class TrieNode():
        def __init__(self):
            self.children = [None]*26 # paremeter to intialize the children
            self.isEnd = False # parameter to keep track of the end of word

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word):
        # check each letter and if the letter is not there in the trie then we create a new trienode and check the next letter in its children and so on, if the letter is already present qwe simply check the next letter till end of the word
        # once all the letters are inserted in the trie, we mark that node's isEnd as true indicating we have a word from root to this child
        """
        :type word: str
        :rtype: None
        """
        curr = self.root

        for w in word:
            idx = ord(w) - ord('a') # to find the idx we subtract the letter asic with a asic as a will be the start idx of the tree 
            if curr.children[idx] is None: 
                curr.children[idx] = self.TrieNode()
            
            curr = curr.children[idx]

        curr.isEnd = True

    def search(self, word):
        # we search each of the letter in the word and see if the letter is present if the letter is not present we return false, if present then by the end we check if its isend is true to check the word exists and not just those letters in the dictionary 
        # for example we are searching for app but we have only word apple in dictionary, then the search for app should return false as p does not have isend true it return false 
        """
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for w in word:
            idx = ord(w) - ord('a')
            if curr.children[idx] is None:
                return False
            curr = curr.children[idx]

        return curr.isEnd
        

    def startsWith(self, prefix):
        # starts wirh a prefix the prefix can be n letter we shoudl check if all those letters of the prefix are in the trie 
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for w in prefix:
            idx = ord(w) - ord('a')
            if curr.children[idx] is None:
                return False
            curr = curr.children[idx]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
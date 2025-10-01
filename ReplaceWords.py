class Solution(object):
    # tc : O(n*l + m*l) [to construct trie where n is the number of words in the dic, l is the average len of the word] +  [to search, m is th enumber of words in the senetcne, l is the average len of those words ]
    # sc : O(n*l + m*l), n*l space taken by trie, m*l soace taken by split array of the sentence 
    # intution 
        # construct the trie for the dictionary of words , and check everyword is present in the dictinoary 
        # for example t is not in the dictinary then we break and wont change that "the" word 
        # for example if we have the word like cattle, and in our dictionary when it start with c and the we foudn isend to be true then we chaneg that word with the ths new word cat
        # thus reducing the larger word with the smallest word

    class TrieNode:
        def __init__(self):
            self.children = [None]*26
            self.isEnd = False

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self,word):
        node = self.root

        for w in word:
            idx = ord(w) - ord('a')
            if node.children[idx] is None :
                node.children[idx] = self.TrieNode()
            node = node.children[idx]
        
        node.isEnd = True

    def search(self, word):
        node = self.root
        short_word = ""

        for w in word:
            idx = ord(w) - ord('a')
            if node.children[idx] is None:
                return word   # no prefix path, return original
            node = node.children[idx]
            short_word += w
            if node.isEnd:
                return short_word

        return word



    def replaceWords(self, dictionary, sentence):

        # build trie first
        for word in dictionary:
            self.insert(word)


        sentence_words = sentence.split(" ") # split the sentence to words
        short_sentence = ""

        for i in range(len(sentence_words)):
            word = sentence_words[i] # check the short version for every word 
            if i != 0: # to make sure we have spaces between the sentences
                short_sentence += " "
            # functin returns the shorter word if present in the dictionary if not return the word itself
            short_sentence += self.search(word)

        return short_sentence



        



# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for i in range(26)]

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for c in word:
            ind = ord(c) - ord("a")
            if not cur.children[ind]:
                cur.children[ind] = TrieNode()
            cur = cur.children[ind]
        cur.is_end = True


    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        s_words = sentence.split()
        for word in dictionary:
            self.insert(word)

        def helper(word):
            rt = ""
            cur = self.root
            for c in word:
                ind = ord(c) - ord("a")
                rt+=c
                if cur and cur.children[ind] and cur.children[ind].is_end:
                    return rt
                if cur:
                    cur = cur.children[ind]

            return word

        
        res = []
        for w in s_words:
            res.append(helper(w))

        return " ".join(res)

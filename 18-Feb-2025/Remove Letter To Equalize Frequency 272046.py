# Problem: Remove Letter To Equalize Frequency - https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution:
    def equalFrequency(self, word: str) -> bool:
        def check(s):
            count=Counter(s)
            freq=set(count.values())
            return len(freq)==1
        
        characters=set(word)
        for char in characters:
            index=0

            for i in range(len(word)):
                if char==word[i]:
                    index=i
                    break

            s=word[:index]+word[index+1:]
            if check(s):
                return True
        
        return False
                

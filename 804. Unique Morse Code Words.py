class Solution:
    def uniqueMorseRepresentations(self, words):
        mos = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        ans = set()
        for word in words:
            decode = ''
            for c in word:
                val = ord(c) - ord('a')
                decode += mos[val]
            ans.add(decode)
        return len(ans)
class Solution(object):
    def findWords(self, words):
        kb = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        ans = []
        for i in kb:
            for word in words:
                fit = True
                for char in word:
                    tmp = char.lower()
                    if tmp not in i:
                        fit = False
                        break
                if fit:
                    ans.append(word)
        return ans
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split()
        ans = []
        n = len(text) - 2
        for i in range(n):
            if text[i] == first and text[i+1] == second:
                ans.append(text[i+2])
        return ans